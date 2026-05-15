# syntax=docker/dockerfile:1
FROM debian:bookworm-slim

ARG MEDIAMTX_VERSION=1.9.3
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates curl \
    python3 python3-pip \
    ffmpeg supervisor \
    bash \
  && rm -rf /var/lib/apt/lists/* \
  && curl -fsSL "https://github.com/bluenviron/mediamtx/releases/download/v${MEDIAMTX_VERSION}/mediamtx_v${MEDIAMTX_VERSION}_linux_amd64.tar.gz" \
    | tar xz -C /usr/local/bin mediamtx \
  && chmod +x /usr/local/bin/mediamtx

WORKDIR /app
ENV PYTHONPATH=/app \
    MITC_DATA_DIR=/data \
    MITC_CAMERAS_FILE=/app/config/cameras.twin.yaml \
    MITC_TWIN_COUNT=8 \
    MITC_ENABLE_WORKER=1 \
    MITC_INGEST_INTERVAL_SEC=12

COPY suite/requirements.txt /app/requirements.txt
RUN pip3 install --no-cache-dir --break-system-packages -r /app/requirements.txt

COPY suite/ /app/
RUN chmod +x /app/entrypoint.sh /app/scripts/twin_feeds.sh

EXPOSE 8080 8554

ENTRYPOINT ["/app/entrypoint.sh"]
