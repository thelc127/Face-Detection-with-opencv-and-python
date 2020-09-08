import cv2

face = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

image = cv2.imread("image.jpg")

grayimage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = face.detectMultiScale(grayimage, 1.1, 4)

for (a,b,c,d) in faces:
	cv2.rectangle(image, (a,b), (a+c, b+d), (255, 0 ,0 ), 2)
	
cv2.imshow('image', image)
cv2.waitKey()