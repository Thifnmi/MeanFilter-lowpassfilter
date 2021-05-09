import cv2
import numpy as np
from matplotlib import pyplot as plt
from scipy import ndimage

# lọc thông thấp
def LowPassFilter(image, x):

    kernel_low_pass_filter = np.asanyarray([1/pow(x+2,2),x/pow(x+2,2),1/pow(x+2,2),x/pow(x+2,2),pow(x,2)/pow(x+2,2)
                                ,x/pow(x+2,2),1/pow(x+2,2),x/pow(x+2,2),1/pow(x+2,2)]).reshape((3,3))
    imgFloat = image.astype(float)
    # nhân tích chập (convolve) 
    conv = ndimage.convolve(imgFloat,kernel_low_pass_filter)
    # điều kiện 
    conv = np.where(conv<0, 0, conv)
    conv = np.where(conv>255, 255, conv)
    conv = conv.astype(np.uint8)
    return conv
