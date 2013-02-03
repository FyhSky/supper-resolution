__licence__ = 'FreeBSD License'
__author__ =  'Robert Gawron'


config = {
    # this PSF is a 5x5 Gaussian
    'psf':   [  2.66971863e-03,   5.36227322e-02,   1.45761699e-01,   5.36227322e-02,    2.66971863e-03,
                5.36227322e-02,   1.07704137e+00,   2.92770198e+00,   1.07704137e+00,    5.36227322e-02,
                1.45761699e-01,   2.92770198e+00,   7.95831909e+00,   2.92770198e+00,    1.45761699e-01,
                5.36227322e-02,   1.07704137e+00,   2.92770198e+00,   1.07704137e+00,    5.36227322e-02,
                2.66971863e-03,   5.36227322e-02,   1.45761699e-01,   5.36227322e-02,    2.66971863e-03 ],


    'offsets_of_captured_imgs' : [[0,0], [1,0], [2,0],
                                  [0,1], [1,1], [2,1],
                                  [0,2], [1,2], [2,2]],

    'scale'          : 2,
    'iterations'     : 10,
    'samples_folder' : './input',
    'output_folder'  : './output'
    }
