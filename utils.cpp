//
//  utils.cpp
//  ImgQualityCheck
//
//  Created by Neeraj Jhawar on 5/4/15.
//  Copyright (c) 2015 SolsSystems. All rights reserved.
//

#include "utils.h"

void show_dimensions(cv::Mat matrix){
    
    std::cout << "matrix dim: "<< matrix.dims << ' ';
    
    for (int i = 0; i < matrix.dims; i++)
        std::cout<< matrix.size[i]<< ' ';
    
}

