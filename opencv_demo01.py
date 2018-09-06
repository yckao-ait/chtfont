import os
import cv2

tp101_1="remi-yuan-569408-unsplash.jpg"
tp101_2="jensen-low-386326-unsplash.jpg"

####################################################
# setup default font file name
basedir = os.path.abspath(os.path.dirname(__file__))
imgFileName = os.path.join(basedir,tp101_2)

img=cv2.imread(imgFileName,-1)

print(type(img))
print(img)
print(img.shape)
print(img.ndim)

resized_img=cv2.resize(img,(1000,500))
cv2.imshow("galaxy",resized_img)
cv2.waitKey(10000)
cv2.destroyAllWindows()