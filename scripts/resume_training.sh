#!/usr/bin/env sh

~/Caffe/build/tools/caffe train --solver=../models/solver.prototxt \
    --snapshot=../models/flower_train_iter_50000.solverstate
