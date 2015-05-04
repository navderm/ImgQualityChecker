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
    image = [UIImage imageNamed:@"1479_r2.png"];
    if (image != nil) {
        _imageView.image = image;
        // Convert UIImage* to cv::Mat
        UIImageToMat(image, cvImage);
        // _imageView.image = image;
        double val = showImage(cvImage);
        NSString *goodImg = @"Good Image";
        NSString *badImg = @"Bad Image";
        NSString *yourString = [NSString stringWithFormat:@"%.10f", val];
        NSString* msgStr;
        if (val > 0.5) {
         msgStr = [NSString stringWithFormat:@"%@ : %@", goodImg, yourString];
        }
        else {
            msgStr = [NSString stringWithFormat:@"%@ : %@", badImg, yourString];
        }
        if (val > 0.5) {
            // Do any additional setup after loading the view, typically from a nib.
            UIAlertView * alert = [[UIAlertView alloc] initWithTitle:@"RESULT!" message:msgStr delegate:self cancelButtonTitle:@"Continue" otherButtonTitles:nil];
            [alert show];
        }
        else {
            // Do any additional setup after loading the view, typically from a nib.
            UIAlertView * alert = [[UIAlertView alloc] initWithTitle:@"RESULT!" message:msgStr delegate:self cancelButtonTitle:@"Continue" otherButtonTitles:nil];
            [alert show];
        }
    }

}

- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

@end
