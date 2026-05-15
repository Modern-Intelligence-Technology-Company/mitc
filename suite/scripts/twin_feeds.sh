#!/bin/bash
# Publish synthetic RTSP into MediaMTX — digital twin of a multi-camera field network.
set -euo pipefail
COUNT="${MITC_TWIN_COUNT:-8}"
echo "twin_feeds: starting ${COUNT} synthetic publishers to rtsp://127.0.0.1:8554/twin_cam_XX"
if [ "${COUNT}" -lt 1 ]; then
  echo "twin_feeds: MITC_TWIN_COUNT<1 — idle (live-camera-only mode; no lavfi publishers)"
  sleep infinity
fi
# Allow mediamtx to open RTSP listener
sleep 4
for i in $(seq 1 "${COUNT}"); do
  idx=$(printf '%02d' "$i")
  (
    while true; do
      ffmpeg -hide_banner -loglevel error -re \
        -f lavfi -i "testsrc2=size=1280x720:rate=12" \
        -c:v libx264 -preset ultrafast -tune zerolatency -pix_fmt yuv420p \
        -f rtsp -rtsp_transport tcp "rtsp://127.0.0.1:8554/twin_cam_${idx}" \
        || sleep 2
    done
  ) &
done
wait
