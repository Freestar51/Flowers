#!/usr/bin/env sh
# Compute the mean image from the imagenet training leveldb
# N.B. this is available in data/ilsvrc12

~/Caffe/build/tools/compute_image_mean ~/Flowers/scripts/flowers_train_lmdb \
  ~/Flowers/data/flowers_mean.binaryproto

echo "Done."
