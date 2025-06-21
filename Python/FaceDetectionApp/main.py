import cv2

trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# To capture video from webcam
webcam = cv2.VideoCapture(0)

# Iterate forever over frames
while True:
    # Read the current frame
    successful_frame_read, frame = webcam.read()

    # Convert RGB to Grayscale
    grayscale_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect Faces
    face_coordinate = trained_face_data.detectMultiScale(grayscale_img)

    # Draw Rectangle around the face
    for (x, y, w, h) in face_coordinate:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 256, 0), 2)

    # Display the image with the faces
    cv2.imshow('Programmer Face Detector', frame)
    key = cv2.waitKey(1)

    # Stop if Q or q key is pressed
    if key == 81 or key == 113:
        break

# Release the VideoCapture object
webcam.release()


