import cv2
import os
import numpy as np
from db import get_fs

# fetch and display a specific frame by filename
def fetch_frame(filename):
    fs = get_fs()
    file = fs.find_one({"filename": filename})
    if file:
        data = file.read()
        frame = cv2.imdecode(np.frombuffer(data, np.uint8), cv2.IMREAD_COLOR)
        cv2.imshow("Frame", frame)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print(f"{filename} not found in MongoDB.")


# display all the stored frames at once
def save_all_frames(output_dir="frames_out"):
    os.makedirs(output_dir, exist_ok=True)

    fs = get_fs()
    for grid_out in fs.find():
        file_path = os.path.join(output_dir, grid_out.filename)
        with open(file_path, "wb") as f:
            f.write(grid_out.read())
        print(f"Saved {grid_out.filename} to {output_dir}")

