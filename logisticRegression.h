//
//  logisticRegression.h
//  ImgQualityCheck
//
//  Created by Neeraj Jhawar on 5/4/15.
//  Copyright (c) 2015 SolsSystems. All rights reserved.
//

#ifndef __realtime_CVProj__logisticRegression__
#define __realtime_CVProj__logisticRegression__

#include <iostream>
#include <opencv2/opencv.hpp>
#include <opencv2/highgui/highgui.hpp>
//#include <opencv/cvaux.hpp>

#endif /* defined(__realtime_CVProj__logisticRegression__) */


class SOLS_logisticRegression{

private:
    std::vector<double> colorModel;
    std::vector<double> colorFeatMean;
    std::vector<double> colorFeatDev;
    
    std::vector<double> textureModel;
    
public:
    SOLS_logisticRegression(int);
    ~SOLS_logisticRegression();
    double getColorProbabilityScore(std::vector<double>);
    
    
    
};