'''
Created on Jan 31, 2017

@author: Gopalakrishna Hegde
'''
import unittest
import lvgui
import cv2

img_path = '../images/lena.jpg'

class UITest(unittest.TestCase):


    def _test_plain_ui_single_win(self):
        '''
        '''
        print('Testing PlainUI class with single window')
        plain_ui = lvgui.PlainUI()
        img = cv2.imread(img_path)
        plain_ui.image = (plain_ui.win_names[0], img)
        
        plain_ui.showall()
        plain_ui.kill()
        
    def _test_plain_ui_multi_win(self):
        print('Testing PlainUI class with two windows')
        ui = lvgui.PlainUI(2, ['win1', 'win2'])
        img1 = cv2.imread('./images/lena.jpg')
        img2 = cv2.imread('./images/lion.jpg')
        ui.image = ('win1', img1)
        ui.image = ('win2', img2)
        ui.showall()
        ui.kill()
        
    def test_slider_ui(self):
        def callback(params):
            pass

            
        print('-'*10+'Testing slider UI'+'-'*10)
        slider_ui = lvgui.SliderUI(plots=('input', 'output'),
            params=('alpha', 'beta', 'gamma'),
            callback=callback,
            title='Test GUI')
        slider_ui.imshow(img_path, 'input')
        slider_ui.show()
        
    
if __name__ == "__main__":
    #print dir()
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()