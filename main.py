import cv2
import os
import numpy as np
print(cv2.__version__)
img = cv2.imread("image.jpg",cv2.IMREAD_COLOR)
B,G,R = cv2.split(img)
zero = np.zeros(img.shape[:2],dtype="uint8")
cv2.imshow("wallpaper",img)

save_directry = "/Users/jinheppell/Desktop/Coding/open cv/images"

os.chdir(save_directry)
cv2.imwrite("landscape.jpg",img)

cv2.imshow("Blue",cv2.merge([B,zero,zero]))
cv2.imshow("Green",cv2.merge([zero,G,zero]))
cv2.imshow("Red",cv2.merge([zero,zero,R]))
cv2.waitKey(0)

cv2.destroyAllWindows()

