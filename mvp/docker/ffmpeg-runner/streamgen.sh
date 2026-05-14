#!/bin/sh
# Publish synthetic H.264 to MediaMTX — production replaces this with a real AXIS RTSP URL.
set -e
sleep 3
exec ffmpeg -hide_banner -loglevel warning -re \
  -f lavfi -i "testsrc2=size=1280x720:rate=10" \
  -c:v libx264 -preset ultrafast -tune zerolatency -pix_fmt yuv420p \
  -f rtsp -rtsp_transport tcp "rtsp://mediamtx:8554/simulated_axis"
