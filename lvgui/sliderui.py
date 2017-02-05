'''
Created on Feb 1, 2017

@author: Gopalakrishna Hegde
'''
from .base import BaseUI
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import math

class SliderUI(BaseUI):
    '''
    classdocs
    '''
    def __init__(self, plots=(), params=(), param_range=(), callback=None, title=None, win_name='Slider GUI'):
        '''
        Constructor
        '''
        # support only one window for this type of UI
        # this class supports multiple subplots instead
        super(SliderUI, self).__init__(1, [win_name])
        self.fig = plt.figure()
        self.fig.suptitle(title, fontsize=12)       
        self.sliders = {}
        self.slider_vals = {}
        
        # main processing method which is to called when the params change 
        self.callback = callback
        
        # artist location related
        self.plot_x_st = 0.1
        self.plot_y_st = 0.3
        self.slider_x_st = 0.2
        self.slider_y_st = 0.05
        self.slider_h = 0.03
        self.slider_w = 0.7
        self.axes_sep = 0.03
        self.plots = {}

        self._create_plots(plots)
        self._create_sliders(params, param_range)
        
    def _create_plots(self, plots):
        num_plots = len(plots)
        if(num_plots == 0):
            return
        best_fit = math.ceil(math.sqrt(num_plots))
        
        sub_plots = [1, 1] 
        if(num_plots == 2):
            sub_plots = [1, 2]
        elif(num_plots > 2):
            sub_plots = [best_fit, best_fit]
        for p, label in enumerate(plots):
            self.plots[label] = self.fig.add_subplot(sub_plots[0], sub_plots[1], p+1)
            self.plots[label].set_title(label)
                
        self.fig.subplots_adjust(left=self.plot_x_st, bottom=self.plot_y_st)
        
    def _create_sliders(self, params, param_range):
        '''
        '''
        n_sliders = len(params)
        s_h = (0.2 - n_sliders * self.axes_sep) / n_sliders
        assert(s_h >= 0), 'Cannot fit sliders'
            
        s_bot  = [self.slider_y_st+(self.slider_h + self.axes_sep)*b for b in range(n_sliders)]        
        
        for s, label in enumerate(params):
            p_min = 0.
            p_max = 1.            
            if(len(param_range) > s):
                p_min = param_range[s][0]
                p_max = param_range[s][1]
            rect = [self.slider_x_st, s_bot[s], self.slider_w, min(s_h, self.slider_h)]            
            ax = self.fig.add_axes(rect, label=label)
            self._add_slider(ax, label, p_min, p_max, 0)
            
    def _add_slider(self, axes, name, val_min, val_max, def_val):
        '''
        '''        
        self.sliders[name] = Slider(axes, name, val_min, val_max, valinit=def_val)
        self.sliders[name].on_changed(self._slider_callback)
        self.slider_vals[name] = def_val
        
    def _slider_callback(self, event):
        '''
        '''
        for s, slider in self.sliders.iteritems():
            self.slider_vals[s] = slider.val
        
        if(self.callback != None):
            self.callback(self.slider_vals)
            
    def plot_img(self, win_name, img):
        '''
        '''
        self.plots[win_name].imshow(img)
        self.plots[win_name].get_xaxis().set_visible(False)
        self.plots[win_name].get_yaxis().set_visible(False)
        #self.fig.canvas.draw_idle()
        #plt.show()
        
    def get_plot(self, win_name):
        return self.plots[win_name]                                 
             
    def imshow(self, img_path, win_name=''):
        '''
        '''        
        img = mpimg.imread(img_path)
        if(win_name == ''):
            win_name = self.plots.keys()[0]
            
        self.plots[win_name].imshow(img)        
        self.show()       
        
    def show(self):
        '''
        '''
        plt.show()    
        
    def kill(self):
        '''
        '''
        plt.close('all')
        
        