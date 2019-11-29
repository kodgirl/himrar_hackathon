import numpy as np
import cv2

def show_im(st, fil):
    cv2.imshow(st, fil)

img = cv2.imread('1.jpg')

final_wide = 600
r = float(final_wide) / img.shape[1]
dim = (final_wide, int(img.shape[0] * r))
img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = cv2.Canny(gray, 100, 200)
#cv2.imshow('3', img)
#eg = cv2.Canny(gray,200,255,apertureSize = 3)
show_im("2", img)
#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
show_im('3', gray)
cors = cv2.goodFeaturesToTrack(gray, 100, 0.2, 30)
cors = np.int0(cors)
for i in cors:
    x, y = i.ravel()
    cv2.circle(img, (x, y), 3, 255, -1)

show_im("1", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
