import cv2
import numpy as np
from db import get_fs
from videoUtils import extract_frames
from fetchFrame import save_all_frames, fetch_frame

fs = get_fs()

VIDEO_PATH = "videos/sample.mp4"
SKIP_FRAMES = 60  # store every 60th frame

for frame_number, frame in extract_frames(VIDEO_PATH, SKIP_FRAMES):
    _, buffer = cv2.imencode(".jpg", frame)
    fs.put(buffer.tobytes(), filename=f"frame_{frame_number}.jpg")
    print(f"Saved frame {frame_number} to MongoDB")

save_all_frames();