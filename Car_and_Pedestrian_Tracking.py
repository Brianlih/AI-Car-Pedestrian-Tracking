from cv2 import cv2 as cv2

img_file = "cars.jpeg"

# pre-trained car classifier
classifier_file = "Car_detector.xml"

img = cv2.imread(img_file)

# 將RGB圖片轉為灰階
black_n_white = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# create a classifier找出車子在圖片的何處
car_tracker = cv2.CascadeClassifier(classifier_file)

# detect car in any size and any scale
cars = car_tracker.detectMultiScale(black_n_white)

for (x, y, w, h) in cars:
    # draw the rectangle around the cars
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)

cv2.imshow("clever programmer car detector", img)
cv2.waitKey()


print("code completed")
