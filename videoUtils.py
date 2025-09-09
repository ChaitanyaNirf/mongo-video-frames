import cv2
import numpy as np

def extract_frames(video_path, skip=30):
    """
    Generator that yields every 'skip'-th frame from the video
    """
    cap = cv2.VideoCapture(video_path)
    count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if count % skip == 0:
            yield count, frame

        count += 1

    cap.release()
