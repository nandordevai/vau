#!/bin/bash

PROCESS2RUN="python3 sr.py"
MONITOR_SCRIPT="monitor.py"

export GOOGLE_APPLICATION_CREDENTIALS=
cd /home/pi/vau
nohup $PROCESS2RUN &
VAR=`pgrep -f "$PROCESS2RUN"`
echo $VAR
nohup python $MONITOR_SCRIPT $VAR &
