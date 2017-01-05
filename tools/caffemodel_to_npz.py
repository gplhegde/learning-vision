import sys, os
import argparse
import numpy as np

def parse_args():
    """Argument parser for this tool
    """
    parser = argparse.ArgumentParser(description='.caffemodel to Numpy .npz model conversion tool.')
    parser.add_argument('--net', dest='net_file', help='Network definition file in .prototxt format.')
    parser.add_argument('--model', dest='model_file', help='Network trained model in .caffemodel format.')

    # parse command line args
    if(len(sys.argv) < 3):
        parser.print_help()
        sys.exit()
    args = parser.parse_args()
    return args


def convert_model(net_file, model_file, npz_name):
    """ Converts .caffemodel into .npz format
    """
    # init the network with the trained model
    caffe.set_mode_cpu()
    net = caffe.Net(net_file, model_file, caffe.TEST)

    numpy_array_list = []
    param_layers = net.params.keys()
    for lyr_name in param_layers:
        print('Layer = {:s}'.format(lyr_name))
        layer = net.layers[list(net._layer_names).index(lyr_name)]
        for b in range(len(layer.blobs)):
            numpy_array_list.append(layer.blobs[b].data)
            print(layer.blobs[b].data.shape)
        
    np.savez(npz_name, *numpy_array_list)

    # verify by reading the model and printing the dimensions
    print('Cross check by reading written npz file. The dimensions below must match the above ones')
    with np.load(npz_name) as mf:
        params = [mf['arr_{:d}'.format(i)] for i in range(len(mf.files))]
        for i in range(len(mf.files)):
            params = mf['arr_{:d}'.format(i)]
            print(params.shape)

    print('Saved caffe model into {:s}'.format(npz_name))

if __name__=='__main__':
    args = parse_args()

    # make sure that path to caffe root directory is set
    assert ('CAFFE_ROOT' in os.environ) , ('Please set CAFFE_ROOT in the environment'
        'variable to point to the caffe installation directory')

    # import caffe package
    caffe_pkg_path = os.path.join(os.environ['CAFFE_ROOT'], 'python')
    if(not os.path.exists):
        print("There is no python package for caffe available. Please compile Caffe with python binding enabled")
        sys.exit()

    sys.path.insert(0, caffe_pkg_path)
    import caffe

    # some sanity check
    assert(os.path.basename(args.model_file).split('.')[-1] == 'caffemodel'), ('Input model'
        'is not caffemodel. Only file with extension .caffemodel is valid')
        
    assert(os.path.basename(args.net_file).split('.')[-1] == 'prototxt'), ('Input net file'
        'is not a prototxt file. Only file with extension .prototxt is valid')

    # create .npz file from .caffemodel
    npz_name = os.path.basename(args.model_file).split('.')[0] + '.npz'
    convert_model(args.net_file, args.model_file, npz_name)
