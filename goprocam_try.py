from goprocam import GoProCamera
import time

gopro = GoProCamera.GoPro()
gopro.stream("udp://127.0.0.1:10000")

import cv2
from goprocam import GoProCamera
gpCam = GoProCamera.GoPro()
vidcap = cv2.VideoCapture("udp://127.0.0.1:10000")

# Check if the connection was successful
if not vidcap.isOpened():
    print("Error: Could not open video stream.")
else:
    frame_count = 0
    start_time = time.time()

    # Loop to read frames until the stream ends or the time limit is reached
    while True:
        success, image = vidcap.read()

        if not success:
            print("Stream ended or failed to read frame.")
            break

        # Increment frame count for each successful read
        frame_count += 1

        # Optional: Set a time limit for capturing frames (e.g., 1 minute)
        elapsed_time = time.time() - start_time
        if elapsed_time >= 60:  # Stop after 1 minute for testing FPM
            break

    # Calculate total elapsed time and frames per minute (FPM) and FPS
    total_time = time.time() - start_time
    fpm = (frame_count / total_time) * 60  # Frames per minute
    fps = frame_count / total_time  # Frames per second

    # Display results
    print(f"Frames per minute (FPM): {fpm:.2f}")
    print(f"Average frames per second (FPS): {fps:.2f}")

    # Release the video capture object
    vidcap.release()