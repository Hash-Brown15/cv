import cv2
import os
print(cv2.__version__)
img = cv2.imread("image.jpg",cv2.IMREAD_COLOR)
B,G,R = cv2.split(img)
cv2.imshow("wallpaper",img)

save_directry = "/Users/jinheppell/Desktop/Coding/open cv/images"

os.chdir(save_directry)
cv2.imwrite("landscape.jpg",img)

cv2.imshow("Blue",B)
cv2.waitKey(0)
cv2.imshow("Green",G)
cv2.waitKey(0)
cv2.imshow("Red",R)
cv2.waitKey(0)

cv2.destroyAllWindows()

