#!/bin/sh
# Commissioning-style probe; exit 0 only when the broker exposes a decodable H.264 video stream.
set -e
sleep 8
exec ffprobe -v error -rtsp_transport tcp -select_streams v:0 \
  -show_entries stream=codec_name,width,height \
  -of default=noprint_wrappers=1 \
  "rtsp://mediamtx:8554/simulated_axis"
