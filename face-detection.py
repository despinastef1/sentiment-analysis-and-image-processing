import cv2
import os

print("Current directory:", os.getcwd())
print("Files in directory:")
print(os.listdir())

group_photo = cv2.imread('pic.jpg')

gray_photo = cv2.cvtColor(group_photo, cv2.COLOR_BGR2GRAY)

# cv2.imshow('Group Photo', gray_photo)
cv2.imwrite('pic_copy.jpg', gray_photo)

# cv2.imwrite('pic.jpg', group_photo)

# cv2.waitKey(0)
# cv2.destroyAllWindows()