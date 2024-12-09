import cv2

# Load the Haar Cascade for face detection
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Start video capture from the webcam
webcam = cv2.VideoCapture(0)

while True:
    # Read a frame from the webcam
    ret, img = webcam.read()

    
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.5,4)
    #draw rectangle
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
    cv2.imshow("Face Detection", img)



    # Wait for 10 milliseconds for a key press
    key = cv2.waitKey(10)

    # Break the loop if the 'Esc' key (ASCII 27) is pressed
    if key == 27:
        break

# Release the webcam and destroy all OpenCV windows
webcam.release()
cv2.destroyAllWindows()

    