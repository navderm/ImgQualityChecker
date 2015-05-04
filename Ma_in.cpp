//
//  Ma_in.cpp
//  ImgQualityCheck
//
//  Created by Neeraj Jhawar on 5/4/15.
//  Copyright (c) 2015 SolsSystems. All rights reserved.
//

#include <stdio.h>
#include <opencv2/opencv.hpp>
#include <opencv2/highgui/highgui.hpp>

#include "features.h"
#include "logisticRegression.h"

#include "Ma_in.h"
#define COLOR_FEATURE 2
#define LBP_FEATURE 1

using namespace cv;
using namespace std;

double showImage (cv::Mat cameraImage)
{
    //Read image
    //Extract Color Feature
    SOLS_RT_Features footFeature(cameraImage);
    std::vector<double> feat = footFeature.getColorFeature();

    SOLS_logisticRegression slr(COLOR_FEATURE);
    double score = slr.getColorProbabilityScore(feat);
//    std::cout << score << std::endl;
//    std::string Type;
//    if (score < 0.5)
//        Type = "BAD Image : ";
//    else
//        Type = "Good Image : ";
//    
//    //std::cout << "score: " << score << "\n" << ' ';
//    std::stringstream ss;
//    ss << score ;
//    std::string txt = ss.str();
//    Type = Type + "Confidence : " + txt;
//    cv::putText(cameraImage, Type, cv::Point(20, 40), CV_FONT_HERSHEY_COMPLEX, 1, cv::Scalar (0, 0 , 255));
//    cv::imshow ("input image", cameraImage);
//    cv::waitKey(-1);
    return score;
}
