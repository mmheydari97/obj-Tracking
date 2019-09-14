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

    # Define the background subtractor object
    bg_subtractor = cv2.createBackgroundSubtractorMOG2()

    # ---------------------------------------------------------------- #
    # history shows the number of previous frames that the model uses  #
    # to learn.                                                        #
    # ---------------------------------------------------------------- #
    history = 100
    learning_rate = 1.0/history

    # Define the scaling factor
    scaling_factor = 0.5

    # Keep reading the frames from the webcam until end
    while True:
        # Grabbing the current frame
        frame = get_frame(cap, scaling_factor)

        # Compute the mask
        mask = bg_subtractor.apply(frame, learning_rate)

        # Convert grayscale image to RGB color image
        mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)

        cv2.imshow('Input', frame)
        cv2.imshow('Output', mask & frame)

        # Check if the user wants to end
        key = cv2.waitKey(5)
        if key == 27:
            break

    # Release the video capture object
    cap.release()

    # Close all the windows
    cv2.destroyAllWindows()
