import cv2
import numpy as np

im = cv2.imread('lena_gray.bmp', cv2.IMREAD_GRAYSCALE)
f = open('lena_gray.raw','wb')
f.write(im)
f.close()