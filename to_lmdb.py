'''
Created on Jul 18, 2015

@author: kashefy
'''
import os
import numpy as np
from scipy import io
import lmdb
from read_img import read_img_cv2

def imgs_to_lmdb(paths_src, path_dst, CAFFE_ROOT=None):
    '''
    Generate LMDB file from set of images
    Source: https://github.com/BVLC/caffe/issues/1698#issuecomment-70211045
    credit: Evan Shelhamer
    '''
    if CAFFE_ROOT is not None:
        import sys
        sys.path.insert(0,  os.path.join(CAFFE_ROOT, 'python'))
    import caffe
    
    db = lmdb.open(path_dst, map_size=int(1e12))
    
    with db.begin(write=True) as in_txn:
    
        for idx, path_ in enumerate(paths_src):
            path_ = '/home/tairuichen/Documents/PASCAL-Context/VOC2010/JPEGImages/'+ path_

            img = read_img_cv2(path_)
            print path_
            #print img.shape
            #print img
            img_dat = caffe.io.array_to_datum(img)
            in_txn.put('{:0>10d}'.format(idx), img_dat.SerializeToString())
    
    db.close()

    return 0

def matfiles_to_lmdb(paths_src, path_dst, fieldname,
                     CAFFE_ROOT=None,
                     lut=None):
    '''
    Generate LMDB file from set of images
    Source: https://github.com/BVLC/caffe/issues/1698#issuecomment-70211045
    credit: Evan Shelhamer
    
    '''
    if CAFFE_ROOT is not None:
        import sys
        sys.path.insert(0,  os.path.join(CAFFE_ROOT, 'python'))
    import caffe
    
    db = lmdb.open(path_dst, map_size=int(1e12))
    
    with db.begin(write=True) as in_txn:
    
        for idx, path_ in enumerate(paths_src):
            path_ = '/home/tairuichen/Documents/PASCAL-Context/trainval/' + path_
            content_field = io.loadmat(path_)[fieldname]
            content_field = np.expand_dims(content_field, axis=0)
            content_field = content_field.astype(int)
            
            if lut is not None:
                content_field = lut(content_field)
            print path_
            #print content_field
            img_dat = caffe.io.array_to_datum(content_field)
            in_txn.put('{:0>10d}'.format(idx), img_dat.SerializeToString())
    
    db.close()

    return 0

