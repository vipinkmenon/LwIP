

#!/usr/bin/python
import numpy as np
import sys
import cv2

# Load image as string from file/database    
fd = open(sys.argv[1],'rb')
img_str = fd.read()
fd.close()

img_array = np.asarray(bytearray(img_str), dtype=np.uint8)

img = img_array.reshape(512,512)

cv2.imshow('rawgrayimage', img)
cv2.waitKey(0)