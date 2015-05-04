//
//  logisticRegression.cpp
//  ImgQualityCheck
//
//  Created by Neeraj Jhawar on 5/4/15.
//  Copyright (c) 2015 SolsSystems. All rights reserved.
//

#include "logisticRegression.h"
#include "utils.h"

SOLS_logisticRegression::SOLS_logisticRegression(int classifierType){

    if(classifierType == 2){
        
        SOLS_logisticRegression::colorModel =
           {-0.85049822, -1.31082448, -1.96558401, -0.70467948, -0.70231494,
            0.08488207,  0.        ,  0.13250223,  0.        , -0.13489663,
            0.        ,  0.        ,  0.        ,  0.        , -0.31103703,
            0.        ,  0.51478419,  0.        ,  0.        ,  0.        ,
            -0.70745382,  0.        ,  0.        ,  0.43658865,  0.26187455,
            0.        ,  0.20614229,  0.15230484,  0.44599612,  0.        ,
            0.27989809,  0.26164675,  0.16250676,  0.45145069,  0.14849254,
            0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
            0.        ,  0.        ,  0.        ,  0.        ,  0.        };
        
        SOLS_logisticRegression::colorFeatMean = {  77.09894737,  142.12143158,  120.84084211,  126.0688    , 90.07709474,  -65.02248421,  -43.74189474,  -48.96985263, -12.97814737,   21.28058947,   16.05263158,   52.04433684,
            -5.22795789,   30.76374737,   35.99170526,  138.82336842,
            133.93709474,  140.58547368,  142.20728421,  140.83431579,
            4.88627368,   -1.76210526,   -3.38391579,   -2.01094737,
            -6.64837895,   -8.27018947,   -6.89722105,   -1.62181053,
            -0.24884211,    1.37296842,  136.86282105,  138.62955789,
            140.42749474,  141.02147368,  138.27326316,   -1.76673684,
            -3.56467368,   -4.15865263,   -1.41044211,   -1.79793684,
            -2.39191579,    0.35629474,   -0.59397895,    2.15423158,2.74821053 };
        
        SOLS_logisticRegression::colorFeatDev = {52.31874844,  59.03919006,  55.93698519,  58.61890165,
            51.87908523,  43.09439123,  30.02863789,  26.00749382,
            18.69024822,  42.08902327,  44.14597567,  42.28847883,
            20.541395  ,  30.30308605,  25.85107839,   7.73605441,
            7.03638634,   7.99334124,   8.24593276,   6.24819409,
            6.93165956,   4.21933545,   4.91201469,   3.95689076,
            6.95340758,   7.85293422,   7.25075409,   3.24686307,
            5.09485307,   4.88298152,   6.36057706,   6.50865427,
            7.08841085,   8.50448132,   6.11134541,   6.85758496,
            5.53343451,   6.92182399,   4.55077829,   7.07561825,
            8.10873767,   7.41317941,   3.40441354,   4.34179926,   5.3168781};
        
        
        
    }
    
    if(classifierType == 1){
        
    }
    
    
}



SOLS_logisticRegression::~SOLS_logisticRegression(){
    
}


double SOLS_logisticRegression::getColorProbabilityScore(std::vector<double> feat){
    
    cv::Mat feat_mat = cv::Mat(feat);
    cv::Mat feat_mean_mat = cv::Mat(SOLS_logisticRegression::colorFeatMean);
    cv::Mat feat_std_mat = cv::Mat(SOLS_logisticRegression::colorFeatDev);
    cv::Mat color_model = cv::Mat(SOLS_logisticRegression::colorModel);
    
    //std::cout << "feat_mat" << ' ';
    //show_dimensions(feat_mat);
    
    cv::Mat tmp;
    cv::subtract(feat_mat, feat_mean_mat, tmp);
    cv::Mat res;
    cv::divide(tmp, feat_std_mat, res);
    
    //std::cout <<  res << ' ';
    
    double score = res.dot(color_model);
    std::cout << "prob of being good : "<< 1 - (1/(1 + exp(-score))) << ' ';
    return 1 - 1/(1 + exp(-score));
    
    
}















