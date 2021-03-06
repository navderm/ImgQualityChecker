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
import urllib
import Image


def trainQualityClassifier(trainFileList, dataRoot):
    
    trainFileGood = trainFileList[0]
    trainFileBad = trainFileList[1]
    
    dataGood = getData(trainFileGood, dataRoot)
    dataBad = getData(trainFileBad, dataRoot)
    labelGood = np.zeros(dataGood.shape[0])
    labelBad = np.ones(dataBad.shape[0])
    
    
    X = np.vstack((dataGood, dataBad))
    y = np.hstack((labelGood, labelBad))
    
    feat_mean = np.mean(X,axis = 0)
    feat_std = np.std(X, axis = 0)
    
    X = (X-feat_mean)*(1./feat_std)
    
    # instantiate a logistic regression model, and fit with X and y
    model = LogisticRegression(C=10, penalty='l1', tol=0.01)
    model = model.fit(X, y)
    
    
    
    return [model, feat_mean, feat_std]
    
    
def valQualityClassifier(model, feat_mean, feat_std, valFileList, dataRoot):
    
    valFileGood = valFileList[0]
    valFileBad = valFileList[1]
    
    dataGood = getData(valFileGood, dataRoot)
    dataBad = getData(valFileBad, dataRoot)
    labelGood = np.zeros(dataGood.shape[0])
    labelBad = np.ones(dataBad.shape[0])
    
    
    X = np.vstack((dataGood, dataBad))
    y = np.hstack((labelGood, labelBad))
    
    
    
    
    X = (X-feat_mean)*(1./feat_std)
    
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
        print el
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
    
    #img_r = img[:,:,0]
    #img_g = img[:,:,1]
    #img_b = img[:,:,2]
    
    """
    io.imshow(img_R); io.show()
    io.imshow(img_G); io.show()
    io.imshow(img_B); io.show()
    """
    
    
    img = color.rgb2lab(img)
    
    img_L = img[:,:,0]
    img_A = img[:,:,1]
    img_B = img[:,:,2]
    
    """
    io.imshow(img_R); io.show()
    io.imshow(img_G); io.show()
    io.imshow(img_B); io.show()
    """
    
    feat = extractImageFeatures(img_L)
    feats.extend(feat)
    
    
    feat = extractImageFeatures(img_A)
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
    
    
    """
    feats = list()
    
    # lbp features
    
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
    
    
    """
    
    # color features
    feats= list()
    avc_1 = np.mean(img1)
    avc_2 = np.mean(img2)
    avc_3 = np.mean(img3)
    avc_4 = np.mean(img4)
    avc_5 = np.mean(img5)
    
    diff1 = avc_1 - avc_2
    diff2 = avc_1 - avc_3
    diff3 = avc_1 - avc_4
    diff4 = avc_1 - avc_5
    diff5 = avc_2 - avc_3
    diff6 = avc_2 - avc_4
    diff7 = avc_2 - avc_5
    diff8 = avc_3 - avc_4
    diff9 = avc_3 - avc_5
    diff10 = avc_4 - avc_5
    
    feats.extend(([avc_1, avc_2, avc_3, avc_4, avc_5, diff1, diff2, diff3, diff4, diff5, diff6, diff7, diff8, diff9, diff10]))
    
    
    
    
    
    
    #plt.bar(range(0,18), hist)
    #plt.show()
    
    return feats

def testQualityClassifier(ext_url):
    
    tmp= pickle.load(open('qualityModel.p', 'rb'))
    model = tmp['model']
    feat_mean = tmp['feat_mean']
    feat_std = tmp['feat_std']
    
    
    import cStringIO
    
    fname = cStringIO.StringIO(urllib.urlopen(ext_url).read())
    im = Image.open(fname)
    feat = constructFeatures(im)
    X = (feat-feat_mean)*(1./feat_std)
    prob = model.predict_proba(X)
    
    
    return prob, im
    
    
    
def wrapper():
    """
    #fname = '/Users/abhishek/SourceLib/realtimeCV/data/qualityClassifier/good/1776_r2.png'
    
    fname = '/Users/abhishek/SourceLib/realtimeCV/data/qualityClassifier/bad/1810_r2.png'
    img = io.imread(fname)
    
    #io.imshow(img)
    #io.show()
    
    
    constructFeatures(img)
    """
    
    dataRoot = '/Users/neeraj_jhawar/Downloads/realtimeCV/data/qualityClassifier/'
    trainFileList = list();
    trainFileList.append('/Users/neeraj_jhawar/Downloads/realtimeCV/data/qualityClassifier/testgood.txt');
    trainFileList.append('/Users/neeraj_jhawar/Downloads/realtimeCV/data/qualityClassifier/testbad.txt')
    model, feat_mean, feat_std = trainQualityClassifier(trainFileList, dataRoot)
    res = dict()
    res['model'] = model;
    res['feat_mean'] = feat_mean;
    res['feat_std'] = feat_std;
    
    
    pickle.dump(res,open('qualityModel.p', 'wb'))
    
    
    valFileList = list();
    valFileList.append('/Users/neeraj_jhawar/Downloads/realtimeCV/data/qualityClassifier/valgood.txt')
    valFileList.append('/Users/neeraj_jhawar/Downloads/realtimeCV/data/qualityClassifier/valbad.txt')
    
    valQualityClassifier(model, feat_mean, feat_std, valFileList, dataRoot)
    
    
    return
    
def wrapper_2():
    
    #URL = 'http://storage.sols.co/fios_mvc/files/profile/00/00/00/24/98/pictures/r2.jpg' #s1
    #URL = 'http://storage.sols.co/fios_mvc/files/profile/00/00/00/27/30/pictures/r2.jpg' #c1
    #URL = 'http://storage.sols.co/fios_mvc/files/profile/00/00/00/43/63/pictures/r2.jpg'#s2
    
    URL = 'http://storage.sols.co/fios_mvc/files/profile/00/00/00/43/94/pictures/r2.jpg' #b1
    #URL = 'http://storage.sols.co/fios_mvc/files/profile/00/00/00/44/06/pictures/r2.jpg' #s3-error
    
    
    
    
    #URL = '/Users/abhishek/SourceLib/realtimeCV/data/qualityClassifier/good/1776_r2.png'
    #URL = 'http://storage.sols.co/fios_mvc/files/profile/00/00/00/27/30/pictures/r2.jpg'
    #URL = 'http://storage.sols.co/fios_mvc/files/profile/00/00/00/43/95/pictures/r2.jpg'
    prob,im = testQualityClassifier(URL)
    
    if prob[0][1] > 0.5:
        verdict = 'decision : BAD quality'
        likelihood = str(prob[0][1])
    else:
        verdict = 'decision : GOOD quality'
        likelihood = str(prob[0][0])
        
    titleStr = verdict + '  Likelihood: '+ likelihood[0:5]
    
    
        
    plt.imshow(im)
    plt.title(titleStr)
    plt.show()
    
    
    
    return
    
#wrapper_2()
