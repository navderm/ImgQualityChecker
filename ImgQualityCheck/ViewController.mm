//
//  ViewController.m
//  ImgQualityCheck
//
//  Created by Neeraj Jhawar on 5/4/15.
//  Copyright (c) 2015 SolsSystems. All rights reserved.
//

#import "ViewController.h"
#import "Ma_in.h"

@interface ViewController () <UIImagePickerControllerDelegate, UINavigationControllerDelegate>
@property (nonatomic, strong) UIImagePickerController *imagePicker;

@end

@implementation ViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    // Do any additional setup after loading the view, typically from a nib.
    // Read the image

//    image = [UIImage imageNamed:@"1479_r2.png"];
//    if (image != nil) {
//        _imageView.image = image;
//        // Convert UIImage* to cv::Mat
//        UIImageToMat(image, cvImage);
//        // _imageView.image = image;
//        double val = showImage(cvImage);
//        if (val > 0.5) {
//            // Do any additional setup after loading the view, typically from a nib.
//            UIAlertView * alert = [[UIAlertView alloc] initWithTitle:@"RESULT!" message:@"Good Image" delegate:self cancelButtonTitle:@"Continue" otherButtonTitles:nil];
//            [alert show];
//        }
//        else {
//            // Do any additional setup after loading the view, typically from a nib.
//            UIAlertView * alert = [[UIAlertView alloc] initWithTitle:@"RESULT!" message:@"Bad Image" delegate:self cancelButtonTitle:@"Continue" otherButtonTitles:nil];
//            [alert show];
//        }
//    }

}
- (IBAction)startImageCapture:(id)sender
{
    self.imagePicker = [[UIImagePickerController alloc] init];
    self.imagePicker.sourceType = UIImagePickerControllerSourceTypeCamera;
    self.imagePicker.mediaTypes = [UIImagePickerController availableMediaTypesForSourceType:
                                   UIImagePickerControllerSourceTypeCamera];
    self.imagePicker.delegate = self;
    [self presentViewController:self.imagePicker animated:YES completion:nil];
}

- (void) imagePickerControllerDidCancel: (UIImagePickerController *) picker
{
    [self dismissViewControllerAnimated:YES completion:nil];
}

// For responding to the user accepting a newly-captured picture or movie
- (void) imagePickerController: (UIImagePickerController *) picker
 didFinishPickingMediaWithInfo: (NSDictionary *) info
{
    // get image data
    UIImage *originalImage = (UIImage *) [info objectForKey:
                                 UIImagePickerControllerOriginalImage];
    UIImage *resizedImage = [self imageWithImage:originalImage scaledToSize:CGSizeMake(1280, 720)];
    
    // process image
    if (resizedImage != nil) {
        _imageView.image = image;
        // Convert UIImage* to cv::Mat
        UIImageToMat(resizedImage, cvImage);
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

    
//    [self dismissViewControllerAnimated:YES completion:nil];

    
}



- (UIImage*)imageWithImage:(UIImage*)image scaledToSize:(CGSize)newSize
{
    UIGraphicsBeginImageContext(newSize);
    [image drawInRect:CGRectMake(0,0,newSize.width,newSize.height)];
    UIImage *newImage = UIGraphicsGetImageFromCurrentImageContext();
    UIGraphicsEndImageContext();
    return newImage;
}

- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

@end
