//
//  features.h
//  realtime_CVProj
//
//  Created by abhishek on 1/29/15.
//  Copyright (c) 2015 SOLS. All rights reserved.
//

#ifndef __realtime_CVProj__features__
#define __realtime_CVProj__features__

#include <iostream>

#include <opencv2/opencv.hpp>
#include <opencv2/highgui/highgui.hpp>
//#include <opencv/cvaux.hpp>
#include <opencv2/core/core.hpp>



#endif /* defined(__realtime_CVProj__features__) */



class SOLS_RT_Features{
    
public:
    SOLS_RT_Features(cv::Mat);
    // 1. featureType : Local-binary-pattern
    // 2. featureType : color-feature
    ~SOLS_RT_Features();
    std::vector<double> getColorFeature();
    std::vector<double> getLbpFeature();
    
    
private:
    void computeLBPfeatures(cv::Mat);
    std::vector<double> computeColorfeatures(cv::Mat);
    std::vector<double> computeColorFeatureChannel(cv::Mat);
    cv::Mat local_image;
 
};