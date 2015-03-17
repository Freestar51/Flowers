#!/bin/bash
PROCNUM=`ps -a | grep caffe | awk '{print $1}'`
LOG_FILE=`ls /tmp | grep $PROCNUM`
LOG_PATH=/tmp/$LOG_FILE
echo $LOG_PATH

~/Flowers/scripts/plot_flowers.py 0 ./accuracy.png $LOG_PATH 
