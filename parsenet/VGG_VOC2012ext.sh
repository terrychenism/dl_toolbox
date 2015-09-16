# You should change $CAFFE_ROOT to the caffe root directory (e.g. ~/project/caffe) or make it as environment variable (e.g. put it in ~/.bashrc)

# if [ ! -d jobs/VGGNet/VOC2012ext ]
# then
#   mkdir -p jobs/VGGNet/VOC2012ext
# fi
../../build/tools/caffe train \
--solver="VGG_VOC2012ext_solver.prototxt" \
--weights="../../models/VGGNet/VGG_ILSVRC_16_layers_fc_reduced.caffemodel" \
--gpu 0 2>&1 | tee ParseNet_context.log


#--weights="../../models/VGGNet/VGG_ILSVRC_16_layers_fc_reduced.caffemodel" \
#--weights="../../models/VGGNet/VGG_ILSVRC_16_layers_conv.caffemodel" \