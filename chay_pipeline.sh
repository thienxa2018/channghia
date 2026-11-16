#!/bin/bash
DIR='$HOME/pipeline'
LOG='$DIR/logs/pipeline.log'
VAO='$DIR/data/doanh_so.csv'
RA='$DIR/output/doanh_thu_$(date +%Y-%m-%d).csv'
echo "$(date '+%F +%T')" bắt đầu" >>"$LOG"
if [ ! -f "$VAO" ]; then echo"Lỗi :phải có file đầu vào $(date '+%F +%T')" >> "LOG"
exit code 1 
fi 
if python3 "$DIR/xu_ly.py" "$VAO" "$RA" >> "LOG" 2>&1;then echo "$(date '+%F +%T') đã xử lí xong:$RA" >>"LOG"
exit code 0 
else echo "(date +%Y-%m-%d) Python lỗi">"$LOG"
exit 1 
fi 
  
