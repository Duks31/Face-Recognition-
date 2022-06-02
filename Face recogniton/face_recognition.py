# # imports 
import cv2


# # load some pretrained data on face frontals from opencv (harr-cascade algorithm)
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# # choose an image to detect face in 
img = cv2.imread('family.jpg')


# # must convert to grey-scale 
grayscale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# # detect face
face_coordinates = trained_face_data.detectMultiScale(grayscale_img)    


# # drawing rectangle around the face 

for (x, y, w, h) in face_coordinates:
    cv2.rectangle(img, (x,y), (x+w, y+h), (128, 255,142), 4)
# # shape       img     img coordinates    color    thickness    


# # show the image 
cv2.imshow('My Face Detector', img)


# # this is to display the image until a key is pressed  
cv2.waitKey(0)


































