from matplotlib import image
import numpy as np
import cv2
import random

def question1():
    # Question 1a
    img = np.zeros((600, 600, 3), dtype = "uint8")
    img[img==0] = 122
    cv2.circle(img, (100, 100), 80, (150, 150, 150), -1)
    circleArea = 80 * 80 * 3.14
    cv2.rectangle(img, (300, 300), (500, 500), (110, 110, 110), -1)
    rectangle1 = (500-300) * (500-300)
    cv2.rectangle(img, (50, 200), (200, 500), (130, 130, 130), -1)
    rectangle2 = (200-50) * (500-200)
    cv2.rectangle(img, (300, 50), (500, 150), (170, 170, 170), -1)
    rectangle3 = (500-300) * (150-50)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("SEG1.jpg", img)
    # Question 1b
    gauss = np.random.normal(0,1,img.size)
    gauss = gauss.reshape(img.shape[0], img.shape[1]).astype('uint8')
    img_gauss = cv2.add(img, gauss)
    cv2.imwrite("SEG2.jpg", img_gauss)
    # Question 1c
    img_gauss_random = img_gauss
    row , col = img_gauss_random.shape
    number_of_pixels = random.randint(300, 10000)
    for i in range(number_of_pixels):
        y_coord=random.randint(0, row - 1)
        x_coord=random.randint(0, col - 1)
        img_gauss_random[y_coord][x_coord] = 255
    number_of_pixels = random.randint(300 , 10000)
    for i in range(number_of_pixels):
        y_coord=random.randint(0, row - 1)
        x_coord=random.randint(0, col - 1)
        img_gauss_random[y_coord][x_coord] = 0
    cv2.imwrite("SEG3.jpg", img_gauss_random)
    return [circleArea, rectangle1, rectangle2, rectangle3]

# Question 2a
def relativeSignedAreaError(true, measured):
    sumofTrue = 0
    for area in true:
        sumofTrue += area
    sumofMeasured = 0
    for area in measured:
        sumofMeasured += area
    top = sumofTrue - sumofMeasured
    areaofError = (top/sumofMeasured) * 100
    return areaofError
    
# Question 2b
def labellingError(incorrect, true):
    return (incorrect/true)

# Question 3a

if __name__ == "__main__":
    areas = question1()
