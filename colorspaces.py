import cv2
import numpy as np


# Define a function to get the current frame from the webcam
def get_frame(cp, sc_f):
    # Read the current frame from the video capture object
    _, frm = cp.read()

    # Resize the image
    frm = cv2.resize(frm, None, fx=sc_f, fy=sc_f,
                     interpolation=cv2.INTER_AREA)

    return frm


if __name__ == '__main__':
    # Define the video capture object
    cap = cv2.VideoCapture(0)

    # Define the scaling factor
    scaling_factor = 0.5

    # Keep reading the frames from the webcam until end
    while True:
        # Grabbing the current frame
        frame = get_frame(cap, scaling_factor)

        # Convert the image to HSV colorspace
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Define range of skin color in hsv
        lower = np.array([0, 70, 60])
        upper = np.array([50, 150, 255])

        # Threshold the hsv image to get only skin color
        mask = cv2.inRange(hsv, lower, upper)

        # Bitwise-AND between the mask and the original image
        img_masked = cv2.bitwise_and(frame, frame, mask=mask)

        # Run median blurring
        img_blurred = cv2.medianBlur(img_masked, 5)

        cv2.imshow('Input', frame)
        cv2.imshow('Output', img_blurred)

        # Check if the user wants to end
        key = cv2.waitKey(10)
        if key == 27:
            break

    # Release the video capture object
    cap.release()

    # Close all the windows
    cv2.destroyAllWindows()
