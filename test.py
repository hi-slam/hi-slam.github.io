import cv2

img = cv2.imread('static/images/9985-hi.png', cv2.IMREAD_UNCHANGED)
print(img.shape)

cv2.imwrite('static/images/hi.png', img[80:700,70:700])