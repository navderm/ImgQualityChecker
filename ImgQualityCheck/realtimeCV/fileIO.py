# -*- coding: utf-8 -*-
"""
Created on Wed Jan 28 16:28:24 2015

@author: abhishek
"""

import os
import shutil


def getTrainingExamples(trainFile):
    
    fList = list();

    fp = open(trainFile, 'r+');
    for line in fp:
        fList.append(line.strip());

    return fList;
    
def partitionByViewPoint(imDir):
    
    imFiles = os.listdir(imDir);
    
    for k in range(len(imFiles)):
        
        if not os.path.isdir(imFiles[k]):
            [inFname, inExt] = os.path.splitext(imFiles[k]);
            # Last two characters form the viewpoint index.
            
            vp = inFname[-2:];
            subDir = imDir + vp.upper();
            dst = subDir;
            src = imDir + imFiles[k];
            
            dstFname = os.path.join(dst, imFiles[k]);
            if not os.path.exists(dstFname):
                shutil.move(src, dst);
    
    
    return;


def getImFileNames(imDir, ext):
    
    #return the names of image files : strip off the extension
    
    allFiles = os.listdir(imDir);
    fileList = list();
    for filename in allFiles:
        [inFname, inExt] = os.path.splitext(filename);
        
        if(inExt == ext):
            fileList.append(inFname);
            

    return fileList;


def writeImageFileList(viewPoint, fileList, sourceDir, targetDir, ext = '.png', train = False):
    
    # Input :

    # viewPoint : 'sock', 'barefoot' etc.
    # fileList : list of filename without extension
    # sourceDir : directory from which filenames were generated
    # targetDir : where the output filelist will be stored
    # ext : extension of the image files
    # train : boolean variable that suggests whether the file will be used for training or testing purposes


    if(train):
        outFileName = 'train' + viewPoint + '.txt';
    else:
        outFileName = 'test' + viewPoint + '.txt';
    
    outFileFullPath = os.path.join(targetDir, outFileName);
    
    fp = open(outFileFullPath, 'a');
    
    for fname in fileList:
        imFile = fname + ext;
        bname = os.path.basename(sourceDir);
        fullImFile = os.path.join(bname, imFile);
        
        fp.write(fullImFile+'\n');
        
    fp.close();
    
    return;
    
    
def generateFileList(rootDirList, targetDir, train = True):
    # input:
    # @param : rootDirs - This is the LIST of directories where the anotations are placed.
    # @param : targetDir - Directory where the list of files will be stored (locally)
    
    
    viewpoints = ['good', 'bad'];
    
    
    for dirname in rootDirList:
        for viewpoint in viewpoints:
            
            fullSubDirname = dirname + '/' + viewpoint;   
            imFileNamesAll = getImFileNames(fullSubDirname, '.png');
            writeImageFileList(viewpoint, imFileNamesAll, fullSubDirname, targetDir, ext = '.png', train = train);

    return;

    

def wrapper():
    """
    imDir = '/Users/abhishek/SourceLib/realtimeCV/data/socks'
    partitionByViewPoint(imDir)
    
    imDir = '/Users/abhishek/SourceLib/realtimeCV/data/barefoot'
    partitionByViewPoint(imDir)
    """
    
    rootDirList = list();
    rootDirList.append('/Users/neeraj_jhawar/Downloads/realtimeCV/data/qualityClassifier');
    #rootDirList.append('/Users/abhishek/SourceLib/realtimeCV/data/barefoot');
    
    targetDir = '/Users/neeraj_jhawar/Downloads/realtimeCV/data/qualityClassifier';

    generateFileList(rootDirList, targetDir, train = False);
    
    
    return



#wrapper()

