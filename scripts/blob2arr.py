#!/usr/bin/env python

'''
import caffe
import numpy as np
import sys

if len(sys.argv) != 3:
	print "Usage: python convert_protomean.py proto.mean out.npy"
	sys.exit()

	blob = caffe.proto.caffe_pb2.BlobProto()
	data = open( sys.argv[1] , 'rb' ).read()
	blob.ParseFromString(data)
	arr = np.array( caffe.io.blobproto_to_array(blob) )
	out = arr[0]
	np.save( sys.argv[2] , out )

'''

from caffe.proto import caffe_pb2
from caffe.io import blobproto_to_array
import numpy as np

blob = caffe_pb2.BlobProto()
data = open("../data/flowers_mean.binaryproto","rb").read()
blob.ParseFromString(data)
nparray = blobproto_to_array(blob)
nparray = nparray.reshape(3,256,256)
f = file("flowers_mean.npy", "wb")
np.save(f, nparray)
f.close()
