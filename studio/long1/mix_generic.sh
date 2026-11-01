#!/bin/bash
# usage: mix_generic.sh <dir> <dur> <out> [seed] [mood]
# Music = core/music2.py (new bed, 2 Nov 2026): voice+bed premixed (bed ~14 dB under voice, ducked on words), then whooshes.
set -e
cd "$1"
printf "file 'lp_a.mp4'\nfile 'lp_b.mp4'\n" > parts.txt
ffmpeg -loglevel error -y -f concat -safe 0 -i parts.txt -c copy noaudio.mp4
python3 -c "import sys; sys.path.insert(0,'/home/claude/sid/v2'); import music2 as M; print(M.mix('vo.mp3', $2, '${4:-$(basename $1)}', '${5:-chill}', 'voicebed.wav'))"
ffmpeg -loglevel error -y -i noaudio.mp4 -i voicebed.wav -i sfx.wav -filter_complex "
[1:a]aresample=44100,acompressor=threshold=0.1:ratio=3:attack=5:release=120[vb];
[2:a]volume=0.35[fx];[vb][fx]amix=inputs=2:normalize=0:duration=first,alimiter=limit=0.95,loudnorm=I=-14:TP=-1.5:LRA=9[a]" \
-map 0:v -map "[a]" -c:v libx264 -preset medium -b:v 3M -maxrate 4.5M -bufsize 8M -pix_fmt yuv420p -c:a aac -b:a 192k -ar 44100 -movflags +faststart -shortest "$3"
echo done
