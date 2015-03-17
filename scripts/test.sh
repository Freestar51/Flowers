#!/usr/bin/env sh

LOG=`top -n 1 | grep caffe`
set -- $LOG
echo $2
