from cv2 import cv2 as cv2

# for image

# img_file = "cars.jpeg"

# # pre-trained car classifier
# classifier_file = "Car_detector.xml"

# img = cv2.imread(img_file)

# # 將RGB圖片轉為灰階
# black_n_white = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# # create a classifier找出車子在圖片的何處
# car_tracker = cv2.CascadeClassifier(classifier_file)

# # detect car in any size and any scale
# cars = car_tracker.detectMultiScale(black_n_white)

# for (x, y, w, h) in cars:
#     # draw the rectangle around the cars
#     cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)

# cv2.imshow("clever programmer car detector", img)
# cv2.waitKey()


# print("code completed")


# for video

video = cv2.VideoCapture("videoplayback.mp4")
classifier_file = "Car_detector.xml"
car_tracker = cv2.CascadeClassifier(classifier_file)

while True:

    # "video.read()" will return a tuple to match with the left one. And every time you read, it will read next frame until the end.
    # The first argument represents if it read successful or not.
    (read_successful, frame) = video.read()
    if read_successful:
        grayscaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        break

    cars = car_tracker.detectMultiScale(grayscaled_frame)
    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

    cv2.imshow('car detector', frame)

    # when the video end, it will close the window.
    cv2.waitKey(1)
