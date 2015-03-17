import os

train = open("../data/train.txt","w")
val = open("../data/val.txt","w")

for label in range(1,18):
	for idx in range(1,61):
		fName = "image_%04d.jpg" % (idx+80*(label-1))
		txtIn = "%s %d\n" % (fName, label)
		train.write(txtIn)
		os.system("mv ../data/%s ../data/train/%s" % (fName, fName))
	for idx in range(61,81):
		fName = "image_%04d.jpg" % (idx+80*(label-1))
		txtIn = "%s %d\n" % (fName, label)
		val.write(txtIn)
		os.system("mv ../data/%s ../data/val/%s" % (fName, fName))

train.close()
val.close()
