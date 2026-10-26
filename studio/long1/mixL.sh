#!/bin/bash
set -e
cd "$(dirname "$0")"
printf "file 'lp_a.mp4'\nfile 'lp_b.mp4'\nfile 'lp_c.mp4'\n" > parts.txt
ffmpeg -loglevel error -y -f concat -safe 0 -i parts.txt -c copy L_noaudio.mp4
ffmpeg -loglevel error -y -i L_noaudio.mp4 -i vo.mp3 -i bedL.wav -i sfxL.wav -filter_complex "
[1:a]aresample=44100,highpass=f=70,acompressor=threshold=0.1:ratio=3:attack=5:release=120,apad=whole_dur=235,volume=1.6,asplit=2[vo][key];
[2:a]volume=0.3[bed];
[bed][key]sidechaincompress=threshold=0.02:ratio=8:attack=15:release=350[bedd];
[3:a]volume=0.6[fx];
[vo][bedd][fx]amix=inputs=3:normalize=0:duration=first,alimiter=limit=0.95,loudnorm=I=-14:TP=-1.5:LRA=9[a]" \
-map 0:v -map "[a]" -c:v libx264 -preset medium -b:v 3M -maxrate 4.5M -bufsize 8M -pix_fmt yuv420p -c:a aac -b:a 192k -ar 44100 -movflags +faststart -shortest same_bro_long_01.mp4
echo done
