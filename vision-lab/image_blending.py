'''
Created on Feb 5, 2017

@author: Gopalakrishna Hegde
'''
import sys
from lvgui import SliderUI
import argparse
import numpy as np
from scipy.misc import imread, imresize


def parse_args():    
    parser = argparse.ArgumentParser(description='Imgae blending demo')
    parser.add_argument('--imgs', dest='imgs', nargs='+', help='Two input images')
    
    if(len(sys.argv) < 4):
        parser.print_help()
        sys.exit()
    args = parser.parse_args()
    if(len(args.imgs) > 2):
        print('Considering first two images for blending')
    return args
    
def main(img1_path, img2_path):
    plots = ('image_1', 'image_2', 'blend')
    params = ('alpha',)
    
    img1 = imread(img1_path)
    img2 = imread(img2_path)
    if(img1.shape != img2.shape):
        com_h = min(img1.shape[0], img2.shape[0])
        com_w = min(img1.shape[1], img2.shape[1])
        assert(img1.shape[2] == img2.shape[2]), 'Cannot blend images with unequal channels'
        if(img1.shape[0] != com_h):
            img1 = imresize(img1, (com_h, com_w))
        else:
            img2 = imresize(img2, (com_h, com_w))        
    
    def update_plots(params):        
        alpha = params['alpha']
        print('New alpha = {:4f}'.format(alpha))
        blend = alpha * img1 + (1 - alpha) * img2
        ui.plot_img(plots[2], blend.astype(np.uint8))
        ui.plot_img(plots[0], img1)
        ui.plot_img(plots[1], img2)
        
        
    ui = SliderUI(plots=plots,
        params=params,
        callback=update_plots,
        title='Image blending demo',
        win_name='Image Blending')
    
    
    blend = 0.0*img1 + 1.0*img2    
    ui.plot_img(plots[0], img1)
    ui.plot_img(plots[1], img2)
    ui.plot_img(plots[2], blend.astype(np.uint8))
    ui.show()
    
if __name__ == '__main__':
    args = parse_args()
    main(args.imgs[0], args.imgs[1])
    