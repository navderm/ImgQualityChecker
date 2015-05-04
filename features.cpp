//
//  features.cpp
//  realtime_CVProj
//
//  Created by abhishek on 1/29/15.
//  Copyright (c) 2015 SOLS. All rights reserved.
//

#include "features.h"


SOLS_RT_Features::SOLS_RT_Features(cv::Mat im){
    
    SOLS_RT_Features::local_image = im;
    
}

std::vector<double> SOLS_RT_Features::getColorFeature(){
    std::vector<double> feat;
    feat = SOLS_RT_Features::computeColorfeatures(SOLS_RT_Features::local_image);
    return feat;
    
}


std::vector<double> SOLS_RT_Features::computeColorfeatures(cv::Mat im){
    
    // Change the color space
    cv::Mat imC = cv::Mat(im.size[1],im.size[0],CV_32SC3);
    cv::cvtColor(im,imC,CV_BGR2Lab);
    
    cv::Mat ch1, ch2, ch3;
    // "channels" is a vector of 3 Mat arrays:
    cv::vector<cv::Mat> channels(3);
    // split img:
    cv::split(imC, channels);
    ch1 = channels[0];
    ch2 = channels[1];
    ch3 = channels[2];
    
    //std::cout << ch3(cv::Rect(1, 1, 5, 5)) << ' ';
    
    /*
    cv::namedWindow( "Display window", CV_WINDOW_AUTOSIZE );
    imshow( "Display window", ch3 );
    cv::waitKey(0);
     */
    
    std::vector<double> feat_ch1, feat_ch2, feat_ch3;
    
    feat_ch1 = computeColorFeatureChannel(ch1);
    feat_ch2 = computeColorFeatureChannel(ch2);
    feat_ch3 = computeColorFeatureChannel(ch3);
    
    feat_ch1.insert(feat_ch1.end(), feat_ch2.begin(), feat_ch2.end());
    feat_ch1.insert(feat_ch1.end(), feat_ch3.begin(), feat_ch3.end());
    
    
    
    
    return feat_ch1;
    
    
    

    
}

std::vector<double> SOLS_RT_Features::computeColorFeatureChannel(cv::Mat im){
    
    
    /*
     
     img1 = img[350:375, 600:625] //600, 350, 25, 25
     img2 = img[250:275, 600:625] //600, 250, 25, 25
     img3 = img[400:425, 600:625] //600, 400, 25, 25
     img4 = img[350:375, 800:825] //800, 350, 25, 25
     img5 = img[350:375, 400:425] //400, 350, 25, 25
     
     */
    
    // Extract the regions
    cv::Mat imR1 = im(cv::Rect(600, 350, 25, 25));
    cv::Mat imR2 = im(cv::Rect(600, 250, 25, 25));
    cv::Mat imR3 = im(cv::Rect(600, 400, 25, 25));
    cv::Mat imR4 = im(cv::Rect(800, 350, 25, 25));
    cv::Mat imR5 = im(cv::Rect(400, 350, 25, 25));
    
    
    // Compute unary features
    cv::Scalar avc_1 = cv::mean(imR1);
    cv::Scalar avc_2 = cv::mean(imR2);
    cv::Scalar avc_3 = cv::mean(imR3);
    cv::Scalar avc_4 = cv::mean(imR4);
    cv::Scalar avc_5 = cv::mean(imR5);
    
    // Compute pairwise features
    
    cv::Scalar diff1 = avc_1 - avc_2;
    cv::Scalar diff2 = avc_1 - avc_3;
    cv::Scalar diff3 = avc_1 - avc_4;
    cv::Scalar diff4 = avc_1 - avc_5;
    cv::Scalar diff5 = avc_2 - avc_3;
    cv::Scalar diff6 = avc_2 - avc_4;
    cv::Scalar diff7 = avc_2 - avc_5;
    cv::Scalar diff8 = avc_3 - avc_4;
    cv::Scalar diff9 = avc_3 - avc_5;
    cv::Scalar diff10 = avc_4 - avc_5;
    
    std::vector<double> out_buf;
    out_buf.push_back(avc_1.val[0]);
    out_buf.push_back(avc_2.val[0]);
    out_buf.push_back(avc_3.val[0]);
    out_buf.push_back(avc_4.val[0]);
    out_buf.push_back(avc_5.val[0]);
    out_buf.push_back(diff1.val[0]);
    out_buf.push_back(diff2.val[0]);
    out_buf.push_back(diff3.val[0]);
    out_buf.push_back(diff4.val[0]);
    out_buf.push_back(diff5.val[0]);
    out_buf.push_back(diff6.val[0]);
    out_buf.push_back(diff7.val[0]);
    out_buf.push_back(diff8.val[0]);
    out_buf.push_back(diff9.val[0]);
    out_buf.push_back(diff10.val[0]);
    
    
    return out_buf;
    
}

void SOLS_RT_Features::computeLBPfeatures(cv::Mat im){
    
}

SOLS_RT_Features::~SOLS_RT_Features(){
    
}

