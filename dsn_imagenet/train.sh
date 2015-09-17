#!/bin/bash

CAFFE_ROOT=../..

$CAFFE_ROOT/build/tools/caffe train \
--gpu=0 \
--solver=solver.prototxt \
2>&1 | tee log.txt

#--snapshot=snapshots/inception_bn_solver_stepsize_6400_iter_1220000.solverstate \
