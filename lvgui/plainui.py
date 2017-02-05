'''
Created on Jan 31, 2017

@author: Gopalakrishna Hegde
'''
from .base import BaseUI
import os
import cv2


class PlainUI(BaseUI):
    '''
    Plain display to show one image without any user input options
    '''

    def __init__(self, no_wins=1, win_names=['Plain Display']):
        '''
        Constructor
        '''
        super(PlainUI, self).__init__(no_wins, win_names)
        for w in range(self.no_wins):            
            cv2.namedWindow(self.win_names[w], cv2.WINDOW_AUTOSIZE)
        self._images = {}    
    
    def add_window(self, name):
        '''
        '''
        cv2.namedWindow(name, cv2.WINDOW_AUTOSIZE)
        self.no_wins += 1
        
    def imshow(self, img_path):
        '''
        '''
        assert(os.path.exists(img_path)), 'File not found'
        img = cv2.imread(img_path)
        cv2.imshow(self.win_names[0], img)
        cv2.waitKey() 
        
    def show(self, win_name):
        '''
        '''
        print 'Shows the image window'
        
    def showall(self):
        '''
        '''
        for w in self.win_names:
            if(self._images.has_key(w)):
                cv2.imshow(w, self._images[w])
        cv2.waitKey()
        
    @property    
    def image(self, win_name):
        '''
        '''
        if(win_name not in self.win_names):
            raise ValueError('Window name is not in the UI')
        return self._images[win_name]
    
    @image.setter
    def image(self, val):
        try:
            win_name, img = val
        except ValueError:
            raise ValueError('Pass a tuple containing window name and image object')
        
        if(win_name not in self.win_names):
            raise ValueError('Window name is not in the UI')
        
        self._images[win_name] = img
        
    def kill(self):
        '''Closes the window for this UI
        '''
        print('Closing all windows...')
        for w in range(self.no_wins):
            cv2.destroyWindow(self.win_names[w])
        