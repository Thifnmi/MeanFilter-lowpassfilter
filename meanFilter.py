import numpy as np
import matplotlib.pyplot as plt
import random
import cv2
import math

# muối tiêu
def SaltAndPaper(image, density):
    # create an empty array with same size as input image
    output = np.zeros(image.shape, np.uint8)

    # parameter for controlling how much salt and paper are added
    threshhold = 1 - density

    # loop every each pixel and decide add the noise or not base on threshhold (density)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            possibility = random.random()
            if possibility < density:
                output[i][j] = 0
            elif possibility > threshhold:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output

# lọc trung bình
def MeanFilter(image, filter_size):
    # create an empty array with same size as input image
    output = np.zeros(image.shape, np.uint8)

    # creat an empty variable
    result = 0

    # deal with filter size = 3x3
    if filter_size == 9:
        for j in range(1, image.shape[0]-1):
            for i in range(1, image.shape[1]-1):
                for y in range(-1, 2):
                    for x in range(-1, 2):
                        result = result + image[j+y, i+x]
                output[j][i] = int(result / filter_size)
                result = 0

    # deal with filter size = 5x5
    elif filter_size == 25:
        for j in range(2, image.shape[0]-2):
            for i in range(2, image.shape[1]-2):
                for y in range(-2, 3):
                    for x in range(-2, 3):
                        result = result + image[j+y, i+x]
                output[j][i] = int(result / filter_size)
                result = 0

    return output

def main():
    # read image
    lena = cv2.imread('lena1000p.jpg')

    # convert to gray image
    gray_lena = cv2.cvtColor(lena, cv2.COLOR_BGR2GRAY)

    # add salt and paper (0.01 is a proper parameter)
    noise_lena = SaltAndPaper(gray_lena, 0.01)

    # use 3x3 mean filter
    mean_3x3_lena = MeanFilter(noise_lena, 9)


    # use 5x5 mean filter
    mean_5x5_lena = MeanFilter(noise_lena, 25)


    # set up side-by-side image display
    fig = plt.figure()
    fig.set_figheight(10)
    fig.set_figwidth(8)

    # # display the oringinal image
    fig.add_subplot(3, 2, 1)
    plt.title('Original Image')
    plt.imshow(gray_lena, cmap='gray')

    # # display the salt and paper image
    fig.add_subplot(3, 2, 2)
    plt.title('Adding Salt & Paper Image')
    plt.imshow(noise_lena, cmap='gray')

    # # display 3x3 mean filter
    fig.add_subplot(3, 2, 3)
    plt.title('3x3 Mean Filter')
    plt.imshow(mean_3x3_lena, cmap='gray')


    # # display 5x5 median filter
    fig.add_subplot(3, 2, 5)
    plt.title('5x5 Mean Filter')
    plt.imshow(mean_5x5_lena, cmap='gray')

    plt.show()


if __name__ == "__main__":
    main()