"""
Created on Jan 31, 2017

@author: Gopalakrishna Hegde
"""

class BaseUI(object):    
    """
    Base UI class using OpenCV methods to display image
    """
    def __init__(self, no_wins=1, win_names=['Display']):
        """
        Constructor
        """
        self.win_names = win_names
        self.no_wins = no_wins    
        
    def imshow(self, img_path):
        """
        """
        raise NotImplementedError('Child needs to implement this')
      
    def show(self):
        """Show the window
        """
        
        raise NotImplementedError('Child needs to implement this')
    
    def kill(self):
        """Close the window
        """
        
        raise NotImplementedError('Child needs to implement this')            

