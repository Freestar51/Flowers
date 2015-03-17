#!/usr/bin/env python

import numpy as np
import random

# Make sure that caffe is on the python path:
caffe_root = '../'  # this file is expected to be in {caffe_root}/examples
import sys

import caffe

# Set the right path to your model definition file, pretrained model weights,
# and the image you would like to classify.
MODEL_FILE = '../models/deploy.prototxt'
PRETRAINED = '../models/flower_train_iter_50000.caffemodel'

num_to_name=[' ','daffodil','snowdrop','lilyvalley','bluebell','crocus','iris',
             'tigerlily','tulip','fritillary','sunflower','daisy','colts_foot',
             'dandelion','cowslip','buttercup','windflower','pansy']

net = caffe.Classifier(MODEL_FILE, PRETRAINED,
                     mean=np.load(caffe_root + '/scripts/flowers_mean.npy'),
                     channel_swap=(2,1,0),
                     raw_scale=255,
					 image_dims=(256, 256))

net.set_phase_test()
net.set_mode_cpu()

err_num=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for idx in range(1,1361):
    IMAGE_FILE = '../jpg/image_'+('%04d')%idx+'.jpg'
    input_image = caffe.io.load_image(IMAGE_FILE)
    prediction = net.predict([input_image], oversample=False)
    if idx/80+1 != prediction[0].argmax():
        err_num[idx/80+1]

for i in range(1,18):
    print 'err rate of class 1: '+str(err_num[idx/80+1]/80)
