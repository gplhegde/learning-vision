'''
Created on Feb 6, 2017

@author: Gopalakrishna Hegde
'''
import sys
from scipy.misc import imread, imresize
import argparse
import numpy as np
from lvgui import SliderUI


def parse_args():    
    parser = argparse.ArgumentParser(description='Gamma correction demo')
    parser.add_argument('--img', dest='img', help='Input image')
    
    if(len(sys.argv) < 3):
        parser.print_help()
        sys.exit()
    args = parser.parse_args()
    return args

def main(img_path):
    '''
    '''
    plots = ('original image', 'transfer func', 'gamma corrected')
    params = ('gamma',)    
    
    input = np.arange(0, 256, 1, dtype=np.float32)    
    img = imread(img_path)
    
    def gamma_correct(p_dict):
        cur_gamma= p_dict[params[0]]        
        output = np.power(input, 1./(cur_gamma + np.finfo(np.float32).eps))
        output_img = np.power(img, 1./(cur_gamma+np.finfo(np.float32).eps))
        output_img = output_img * 255 / (np.amax(output_img) + np.finfo(np.float32).eps)
        
        ui.plot_img(plots[2], output_img.astype(np.uint8))
        tx_fn.set_ydata(output)        
        
    ui = SliderUI(plots=plots,
        params=params,
        callback=gamma_correct,
        param_range=([0, 10],),
        title='Gamma connection demo',
        win_name='Gamma correction')
    
    ui.plot_img(plots[0], img)
    ui.plot_img(plots[2], img)
    tx_fn_plot = ui.get_plot(plots[1])
    tx_fn, = tx_fn_plot.plot(input, input, 'b')
    ui.show()
        
if __name__ == '__main__':
    args = parse_args()
    main(args.img)