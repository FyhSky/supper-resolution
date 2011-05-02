#!/usr/bin/env python
__version__ =  '0.1'
__licence__ = 'FreeBSD License'
__author__ =  'Robert Gawron'

import Image
import yaml
import math
import random

class KnownInputEstimationTester:
    """Take as input.."""
    pass

class UnknownInputEstimationTester:
    def __init__(base_img, sample_imgs):
        pass
    def compare():
        pass

class MotionEstimator:
    def __init__(self, iteraions_per_check=9):
        self.iteraions_per_check = iteraions_per_check
        self.mask = ((0, 0), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))
 

    def compute_offset(self, a, b, start_point):
        width, height = a.size
        x_start, y_start = start_point
        x, y = x_start, y_start 

        p1, p2 = a.getpixel((x, y)), b.getpixel((x, y))
        difference = abs(p1[0] - p2[0])
        smalest_difference = difference

        for i in range(self.iteraions_per_check):
            p = i % len(self.mask)
            x_checked, y_checked = x + self.mask[p][0], y + self.mask[p][1]
            p1, p2 = a.getpixel((x, y)), b.getpixel((x_checked, y_checked))
            difference = abs(p1[0] - p2[0])

            if difference < smalest_difference:
                smalest_difference = difference
                x, y = x_checked, y_checked

        return x - x_start, y - y_start


    def estimate(self, a, b):
        iterations=100

        width, height = a.size
        a = a.resize((width*2, height*2)) 
        b = b.resize((width*2, height*2)) 

        width, height = a.size
        w = 4
        x, y = 0, 0

        for i in range(iterations):
            p = random.randrange(w, width-w), random.randrange(w, height-w)
            xn, yn = self.compute_offset(a, b, p)
            x, y = x + xn, y + yn

        return x / iterations, y / iterations

if __name__=="__main__":
    default_config_path = 'motion_estimator_config.yaml'
    config = open(default_config_path, 'r')
    config = yaml.load(config)

    samples = map(lambda u: config['samples_directory'] +u, config['samples_names'])
    images = map(Image.open, samples)

    
    estimator = MotionEstimator()

    sum_of_errors = 0 
    for i in range(1, len(samples)):
        x, y = estimator.estimate(images[0], images[i])
        expectation = config['samples_movments'][i]
        error = abs(x - expectation[0]) + abs(y - expectation[1])
        sum_of_errors += error
        print "(%2d %2d) -> (%2d, %2d) %d" % (expectation[0], expectation[1], x, y, error)
  
    print "total: %d" % sum_of_errors 