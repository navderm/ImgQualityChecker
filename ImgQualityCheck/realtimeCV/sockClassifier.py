# -*- coding: utf-8 -*-
"""
Created on Wed Jan 28 16:21:56 2015

@author: abhishek
"""


# Standard python library
from skimage import io, transform, color;
from skimage.feature import local_binary_pattern
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
import os;

import pickle;
import glob;
import numpy as np;
from fileIO import *;




def trainSockClassifier(trainFileList, dataRoot):
    
    trainFileSocks = trainFileList[0]
    trainFileBarefoot = trainFileList[1]
    
    dataSocks = getData(trainFileSocks, dataRoot)
    dataBarefoot = getData(trainFileBarefoot, dataRoot)
    labelSocks = np.zeros(dataSocks.shape[0])
    labelBarefoot = np.ones(dataBarefoot.shape[0])
    
    
    X = np.vstack((dataSocks, dataBarefoot))
    y = np.hstack((labelSocks, labelBarefoot))
    
    # instantiate a logistic regression model, and fit with X and y
    model = LogisticRegression(C=10, penalty='l1', tol=0.01)
    model = model.fit(X, y)
    
    tmp = dict()
    tmp['model'] = model
    pickle.dump(tmp,open('sockModel.p', 'wb'))
    
    
    return model
    
    
def valSockClassifier(model, valFileList, dataRoot):
    
    valFileSocks = valFileList[0]
    valFileBarefoot = valFileList[1]
    
    dataSocks = getData(valFileSocks, dataRoot)
    dataBarefoot = getData(valFileBarefoot, dataRoot)
    
    labelSocks = np.zeros(dataSocks.shape[0])
    labelBarefoot = np.ones(dataBarefoot.shape[0])
    
    
    X = np.vstack((dataSocks, dataBarefoot))
    y = np.hstack((labelSocks, labelBarefoot))
    
    
    # check the accuracy on the training set
    sc = model.score(X, y)
    print sc
    
    prob = model.predict_proba(X)
    print prob
    
    return

def getData(trainFile, dataRoot):
    
    fList = getTrainingExamples(trainFile);
    
    
    Feats = np.array([]);
    for el in fList:
        
        el = os.path.join(dataRoot,el)
        img = io.imread(el)
        feats = constructFeatures(img)
        if len(Feats) == 0:
            Feats = feats;
        else:
            Feats = np.vstack((Feats,feats))
    
    
    return Feats

def constructFeatures(img):
    
    feats = list()
    img_R = img[:,:,0]
    img_G = img[:,:,1]
    img_B = img[:,:,2]
    
    feat = extractImageFeatures(img_R)
    feats.extend(feat)
    
    
    feat = extractImageFeatures(img_G)
    feats.extend(feat)
    
    
    feat = extractImageFeatures(img_B)
    feats.extend(feat)
    
    
    return feats

def extractImageFeatures(img):
    
    #patch 1 :
    img1 = img[350:375, 600:625]
    img2 = img[250:275, 600:625]
    img3 = img[400:425, 600:625]
    img4 = img[350:375, 800:825]
    img5 = img[350:375, 400:425]
    
    radius = 2
    n_points = 8 * radius
    METHOD = 'uniform'
    
    
    
    feats = list()
    
    
    lbp = local_binary_pattern(img1, n_points, radius, METHOD)
    n_bins = lbp.max() + 1
    hist1, _ = np.histogram(lbp, normed=True, bins=n_bins, range=(0, n_bins))
    feats.extend(hist1)
    
    lbp = local_binary_pattern(img2, n_points, radius, METHOD)
    n_bins = lbp.max() + 1
    hist2, _ = np.histogram(lbp, normed=True, bins=n_bins, range=(0, n_bins))
    feats.extend(hist2)
    
    lbp = local_binary_pattern(img3, n_points, radius, METHOD)
    n_bins = lbp.max() + 1
    hist3, _ = np.histogram(lbp, normed=True, bins=n_bins, range=(0, n_bins))
    feats.extend(hist3)
    
    
    lbp = local_binary_pattern(img4, n_points, radius, METHOD)
    n_bins = lbp.max() + 1
    hist4, _ = np.histogram(lbp, normed=True, bins=n_bins, range=(0, n_bins))
    feats.extend(hist4)
    
    lbp = local_binary_pattern(img5, n_points, radius, METHOD)
    n_bins = lbp.max() + 1
    hist5, _ = np.histogram(lbp, normed=True, bins=n_bins, range=(0, n_bins))
    feats.extend(hist5)
    
    
    
    #plt.bar(range(0,18), hist)
    #plt.show()
    
    return feats

def testSockClassifier(ext_url):
    
    tmp= pickle.load(open('sockModel.p', 'rb'))
    model = tmp['model']
    
    
    
    import cStringIO
    import urllib
    import Image
    
    fname = cStringIO.StringIO(urllib.urlopen(ext_url).read())
    im = Image.open(fname)
    im = np.asarray(im)
    feat = constructFeatures(im)
    X = feat
    prob = model.predict_proba(X)
    
    
    return prob, im
    
    
    
def wrapper():
    
    
    """
    #fname = '/Users/abhishek/SourceLib/MultiviewScaling/New_Feet/L2.jpg'
    
    fname = '/Users/abhishek/SourceLib/MultiviewScaling/barefootIm_SOLS/L2/1844_l2.png'
    img = io.imread(fname)
    
    io.imshow(img)
    io.show()
    
    
    feats = constructFeatures(img)
    """
    
    dataRoot = '/Users/abhishek/SourceLib/realtimeCV/data/sockClassification/'
    trainFileList = list();
    trainFileList.append('/Users/abhishek/SourceLib/realtimeCV/data/sockClassification/testsocks.txt');
    trainFileList.append('/Users/abhishek/SourceLib/realtimeCV/data/sockClassification/testbarefoot.txt')
    model = trainSockClassifier(trainFileList, dataRoot)
    
    valFileList = list();
    valFileList.append('/Users/abhishek/SourceLib/realtimeCV/data/sockClassification/valsocks.txt')
    valFileList.append('/Users/abhishek/SourceLib/realtimeCV/data/sockClassification/valbarefoot.txt')
    
    valSockClassifier(model, valFileList, dataRoot)
    
    
    return
    
def wrapper_2():
    
    #URL = 'http://storage.sols.co/fios_mvc/files/profile/00/00/00/24/98/pictures/r2.jpg' #s1 
    #URL = 'http://storage.sols.co/fios_mvc/files/profile/00/00/00/27/30/pictures/r2.jpg'#c1
    #URL = 'http://storage.sols.co/fios_mvc/files/profile/00/00/00/43/63/pictures/r2.jpg'#s2
    
    URL = 'http://storage.sols.co/fios_mvc/files/profile/00/00/00/43/94/pictures/r2.jpg' #b1
    #URL = 'http://storage.sols.co/fios_mvc/files/profile/00/00/00/44/06/pictures/r2.jpg' #s3-error
    
    
    
    #URL = '/Users/abhishek/SourceLib/realtimeCV/data/qualityClassifier/good/1776_r2.png'
    #URL = 'http://storage.sols.co/fios_mvc/files/profile/00/00/00/43/95/pictures/r2.jpg'
    
    #URL = 'http://storage.sols.co/fios_mvc/files/profile/00/00/00/24/98/pictures/r2.jpg'
    
    
    prob,im = testSockClassifier(URL)
    
    
    
    if prob[0][1] < 0.5:
        verdict = 'decision : Socks'
        likelihood = str(prob[0][0]);
    else:
        verdict = 'decision: bareFoot'
        likelihood = str(prob[0][1]);
       
    titleStr = verdict + '  Likelihood: '+likelihood[0:5]
        
    plt.imshow(im)
    plt.title(titleStr)
    plt.show()
    
    
    return    
    
#wrapper_2()














