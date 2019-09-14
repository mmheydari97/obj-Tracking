import numpy as np
import cv2


# Load the Haar cascade files
face_cascade = cv2.CascadeClassifier(
    './haar_cascade_files/haarcascade_frontalface_default.xml')

eye_cascade = cv2.CascadeClassifier(
    './haar_cascade_files/haarcascade_eye.xml')

nose_cascade = cv2.CascadeClassifier(
    './haar_cascade_files/haarcascade_mcs_nose.xml')


# Check if the cascade file has been loaded correctly

for a in (face_cascade, eye_cascade, nose_cascade):
    if a.empty():
        raise IOError('Unable to load the face cascade classifier xml file')

# Initialize the video capture object
cap = cv2.VideoCapture(0)

# Define the scaling factor
scaling_factor = 0.5

# Iterate until the user hits the 'Esc' key
while True:
    # Capture the current frame
    _, frame = cap.read()

    # Resize the frame
    frame = cv2.resize(frame, None, fx=scaling_factor,
                       fy=scaling_factor, interpolation=cv2.INTER_AREA)

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Run the face detector on the grayscale image
    face_rects = face_cascade.detectMultiScale(gray, 1.3, 5)

    # Run the eye detector on the grayscale image
    eye_rects = eye_cascade.detectMultiScale(gray, 1.3, 5)

    # Run the nose detector on the grayscale image
    nose_rects = nose_cascade.detectMultiScale(gray, 1.3, 5)

    # Draw a blue rectangle around the face
    for (x, y, w, h) in face_rects:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 3)

    # Draw a green rectangle around the eyes
    for (x, y, w, h) in eye_rects:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)

    # Draw a red rectangle around the nose
    for (x, y, w, h) in nose_rects:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 3)

    # Display the output
    cv2.imshow('Face Detector', frame)

    # Check if the user hit the 'Esc' key
    key = cv2.waitKey(5)
    if key == 27:
        break

# Release the video capture object
cap.release()

# Close all the windows
cv2.destroyAllWindows()
