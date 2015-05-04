//
//  utils.cpp
//  realtime_CVProj
//
//  Created by abhishek on 1/31/15.
//  Copyright (c) 2015 SOLS. All rights reserved.
//

#include "utils.h"

void show_dimensions(cv::Mat matrix){
    
    std::cout << "matrix dim: "<< matrix.dims << ' ';
    
    for (int i = 0; i < matrix.dims; i++)
        std::cout<< matrix.size[i]<< ' ';
    
}

