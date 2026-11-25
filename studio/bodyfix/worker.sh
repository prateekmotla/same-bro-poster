#!/bin/bash
# render worker: picks b*/ with vo.mp3 and no short.mp4, renders. Exits when all 50 have short.mp4 or after idle 40 min.
cd /home/claude/sid/shorts
idle=0
while true; do
  done_n=$(ls b*/short.mp4 2>/dev/null | wc -l)
  [ "$done_n" -ge 50 ] && exit 0
  picked=""
  for d in $(ls -d b[0-9][0-9]_* | sort); do
    [ -f "$d/vo.mp3" ] || continue
    [ -f "$d/short.mp4" ] && continue
    if mkdir "$d/.lock" 2>/dev/null; then picked=$d; break; fi
  done
  if [ -z "$picked" ]; then sleep 20; idle=$((idle+20)); [ $idle -gt 2400 ] && exit 0; continue; fi
  idle=0
  echo "$(date +%T) start $picked" >> render.log
  if python3 $picked/make.py render > $picked/render.out 2>&1; then echo "$(date +%T) done $picked" >> render.log
  else echo "$(date +%T) FAIL $picked" >> render.log; rm -f $picked/short.mp4; fi
done
