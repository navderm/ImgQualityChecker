# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 14:15:28 2015

@author: abhishek
"""
from sockClassifier import *
from illuminationClassifier import *


def demo():
    
    
    #URL = 'http://storage.sols.co/fios_mvc/files/profile/00/00/00/24/98/pictures/r2.jpg' #s1 
    #URL = 'http://storage.sols.co/fios_mvc/files/profile/00/00/00/43/94/pictures/r2.jpg' #b1
    #URL = 'http://storage.sols.co/fios_mvc/files/profile/00/00/00/43/65/pictures/r2.jpg' #b2
    #URL = 'http://storage.sols.co/fios_mvc/files/profile/00/00/00/43/63/pictures/r2.jpg'#s2    
    
    
    #URL = 'http://storage.sols.co/fios_mvc/files/profile/00/00/00/27/30/pictures/r2.jpg'#c1
    #
    
    
    #URL = 'http://storage.sols.co/fios_mvc/files/profile/00/00/00/44/06/pictures/r2.jpg' #s3-error
    #URL = 'http://storage.sols.co/fios_mvc/files/orders/00/00/00/23/22/pictures/r2.jpg' #b3-error
    
    #Bad quality examples:
    #URL = '/Users/abhishek/SourceLib/realtimeCV/data/qualityClassifier/bad/1859_r2.png'
    #URL = '/Users/abhishek/SourceLib/realtimeCV/data/qualityClassifier/bad/1628_r2.png'
    #URL = '/Users/abhishek/SourceLib/realtimeCV/data/qualityClassifier/bad/1682_r2.png'
    
    #URL = '/Users/abhishek/SourceLib/realtimeCV/data/qualityClassifier/bad/1859_r2.png'
    URL = '/Users/abhishek/SourceLib/realtimeCV/data/qualityClassifier/good/1631_r2.png'
    
    
    #URL = '/Users/abhishek/SourceLib/realtimeCV/data/qualityClassifier/bad/'
    prob,im_f = testSockClassifier(URL)
    
    
    
    if prob[0][1] < 0.5:
        verdict = 'decision : Socks'
        likelihood = str(prob[0][0]);
    else:
        verdict = 'decision: bareFoot'
        likelihood = str(prob[0][1]);
       
    titleStr_f = verdict + '  Likelihood: '+likelihood[0:5]
    
    """    
    plt.imshow(im)
    plt.title(titleStr)
    plt.show()
    """
    
    prob,im_s = testQualityClassifier(URL)
    
    if prob[0][1] > 0.5:
        verdict = 'decision : bad quality'
        likelihood = str(prob[0][1])
    else:
        verdict = 'decision : good quality'
        likelihood = str(prob[0][0])
        
    titleStr_s = verdict + '  Likelihood: '+ likelihood[0:5]
    
    titleStr = titleStr_f + '\n' + titleStr_s
    
       
    plt.imshow(im_f)
    plt.title(titleStr)
    plt.show()
    
    
    
    return
    
demo()  
