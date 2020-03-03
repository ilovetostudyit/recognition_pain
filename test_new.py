import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
face_cascade_2 = cv2.CascadeClassifier('haarcascade_profileface.xml')
# Read the input image
cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame1 = cap.read()
    if frame1 is not None:
        img = cv2.resize(frame1, (240, 240), interpolation = cv2.INTER_AREA)
        # Convert into grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #    # Detect faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        faces_2 = face_cascade_2.detectMultiScale(gray, 1.1, 4)
        # Draw rectangle around the faces
        #    x1 = 0
            #print ("[I CAN SEE YOU], face in the frame")
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        for (x, y, w, h) in faces_2:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 255, 0), 2)
        #else:
        #    print ("[I CAN'T SEE YOU], bitch")
        # Display the output
    cv2.imshow('img', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
#cv2.destroyAllWindows()