'''
Created on Feb 7, 2017

@author: Gopalakrishna Hegde
'''
import sys
from scipy.misc import imread, imresize
import argparse
import numpy as np
from skimage import exposure
from skimage import data, img_as_float
from lvgui import SliderUI

def parse_args():    
    parser = argparse.ArgumentParser(description='Histogram equalization demo')
    parser.add_argument('--img', dest='img', help='Input image')
    
    if(len(sys.argv) < 3):
        parser.print_help()
        sys.exit()
    args = parser.parse_args()
    return args

def main(img_path):
    plots = ('Input image', 'input histogram', 'transfer fucc', 'simple equalized', 'adaptive equalized')
    params = ('local window size',)
    
    org_img = imread(img_path)
    
    
    def update_plots(p_dict):
        win_size = int(p_dict[params[0]])
        ada_hist = exposure.equalize_adapthist(org_img, kernel_size=win_size)
        ui.plot_img(plots[4], ada_hist)
    
    ui = SliderUI(plots=plots,              
        params=params,
        param_range=([3, 25],),
        callback=update_plots,  
        title='Histogram equalization demo',
        win_name='Histogram equalization')
    
    output_img = exposure.equalize_hist(org_img)
    ada_hist = exposure.equalize_adapthist(org_img, kernel_size=5)
    
    ui.plot_img(plots[0], org_img)    
    ui.plot_img(plots[3], output_img)
    ui.plot_img(plots[4], ada_hist)
    ui.show()    
if __name__ == '__main__':
    args = parse_args()
    main(args.img)
    