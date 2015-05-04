//
//  ViewController.m
//  ImgQualityCheck
//
//  Created by Neeraj Jhawar on 5/4/15.
//  Copyright (c) 2015 SolsSystems. All rights reserved.
//

#import "ViewController.h"

@interface ViewController ()

@end

@implementation ViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    // Do any additional setup after loading the view, typically from a nib.
    // Read the image
    image = [UIImage imageNamed:@"realtimeCV/data/qualityClassifier/good/1479_r2.png"];
    if (image != nil) {
        _imageView.image = image;
        // Convert UIImage* to cv::Mat
        UIImageToMat(image, cvImage);
        
        double val = showImage(cvImage);
        if (val > 0.5) {
            // Do any additional setup after loading the view, typically from a nib.
            UIAlertView * alert = [[UIAlertView alloc] initWithTitle:@"RESULT!" message:@"Good Image" delegate:self cancelButtonTitle:@"Continue" otherButtonTitles:nil];
            [alert show];
        }
        else {
            // Do any additional setup after loading the view, typically from a nib.
            UIAlertView * alert = [[UIAlertView alloc] initWithTitle:@"RESULT!" message:@"Bad Image" delegate:self cancelButtonTitle:@"Continue" otherButtonTitles:nil];
            [alert show];
        }
            
//
//        cv::Mat blurredImg;
//        cv::blur (cvImage, blurredImg, cv::Size(5,5));
//        image = MatToUIImage(blurredImg);
        _imageView.image = image;
    }

}

- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

@end
