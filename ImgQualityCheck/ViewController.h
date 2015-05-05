//
//  ViewController.h
//  ImgQualityCheck
//
//  Created by Neeraj Jhawar on 5/4/15.
//  Copyright (c) 2015 SolsSystems. All rights reserved.
//
#import <UIKit/UIKit.h>
#ifdef __cplusplus
#include <opencv2/highgui/ios.h>
#include <opencv2/opencv.hpp>
#include <opencv2/opencv_modules.hpp>

#include "Ma_in.h"
#include <iostream>
// using namespace cv;
#endif
#import <Foundation/Foundation.h>

@interface ViewController : UIViewController
{
    UIImage* image;
    cv::Mat cvImage;
}

@property (nonatomic, weak) IBOutlet UIImageView* imageView;
@end