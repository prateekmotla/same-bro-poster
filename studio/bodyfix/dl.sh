#!/bin/bash
# usage: dl.sh NO URL  -> downloads raw.mp3, speeds 1.08x into vo.mp3
d=$(ls -d /home/claude/sid/shorts/b$(printf %02d $1)_* | head -1)
curl -sSL -o "$d/raw.mp3" "$2" && ffmpeg -y -loglevel error -i "$d/raw.mp3" -af atempo=1.08 -b:a 192k "$d/vo.tmp.mp3" && mv "$d/vo.tmp.mp3" "$d/vo.mp3" && echo "vo $1 $(ffprobe -v error -show_entries format=duration -of csv=p=0 $d/vo.mp3)"
