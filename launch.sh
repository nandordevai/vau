#!/bin/bash

PROCESS2RUN="python sr.py"
MONITOR_SCRIPT="monitor.py"

cd /home/pi/vau
nohup $PROCESS2RUN &
VAR=`pgrep -f "$PROCESS2RUN"`
echo $VAR
nohup python $MONITOR_SCRIPT $VAR &
