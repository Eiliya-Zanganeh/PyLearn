import cv2 as cv

image = cv.imread('cats.png')
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cat_detector = cv.CascadeClassifier('haarcascade_frontalcatface.xml')
cats = cat_detector.detectMultiScale(gray)
for (x, y, w, h) in cats:
    cv.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 3)
cv.putText(image, f'cat count: {len(cats)}', (50, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
cv.imshow('image', image)
cv.waitKey(0)
