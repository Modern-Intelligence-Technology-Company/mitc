# Lightweight ffmpeg/ffprobe for lab RTSP (no upstream ENTRYPOINT surprises).
FROM alpine:3.19
RUN apk add --no-cache ffmpeg
COPY streamgen.sh smoke.sh /
RUN chmod +x /streamgen.sh /smoke.sh
