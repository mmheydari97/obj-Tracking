import cv2


# Compute the frame differences
def frame_diff(prev_frame, cur_frame, next_frame):
    diff_frames_1 = cv2.absdiff(next_frame, cur_frame)
    diff_frames_2 = cv2.absdiff(cur_frame, prev_frame)

    return cv2.bitwise_and(diff_frames_1, diff_frames_2)


# Define a function to get the current frame from the webcam
def get_frame(cap, scaling_factor):
    # Read the current frame from the video capture object
    _, frame = cap.read()

    # Resize the image
    frame = cv2.resize(frame, None, fx=scaling_factor, fy=scaling_factor,
                       interpolation=cv2.INTER_AREA)

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    return gray


if __name__ == '__main__':
    # Define the video capture object
    cap = cv2.VideoCapture(0)

    # Define the scaling factor
    scaling_factor = 0.5

    # Grabbing 3 frames
    prev_frame = get_frame(cap, scaling_factor)
    cur_frame = get_frame(cap, scaling_factor)
    next_frame = get_frame(cap, scaling_factor)

    # Keep reading the frames from the webcam until end
    while True:
        # Display the frame difference
        cv2.imshow('Object Movement', frame_diff(prev_frame, cur_frame, next_frame))

        # Updating frame vars
        prev_frame = cur_frame
        cur_frame = next_frame

        next_frame = get_frame(cap, scaling_factor)

        # Check if the user wants to end
        key = cv2.waitKey(10)
        if key == 27:
            break

    # Close all the windows
    cv2.destroyAllWindows()
