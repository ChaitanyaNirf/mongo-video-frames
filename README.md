# 🎥 Video Frame Storage with MongoDB

This project demonstrates how to parse a video into frames, store them in **MongoDB (GridFS)**, and later fetch them back into a local folder.  
It’s a small end-to-end pipeline that shows database usage with binary data.

---

## 🚀 Features
- Extract frames from a video using **OpenCV**  
- Store frames in **MongoDB GridFS**  
- Retrieve frames from the database  
- Dump frames back into a folder for inspection  

---

## 📂 Project Structure
```
.
├── db.py             # Database connection + GridFS setup
├── videoUtils.py    # Logic to extract frames and store them in MongoDB
├── fetchFrames.py    # Logic to fetch frames from MongoDB and dump into folder
├── requirements.txt  # Python dependencies
└── README.md
```

---

## 🛠️ Setup

### 1. Clone the repo
```bash
git clone https://github.com/ChaitanyaNirf/mongo-video-frames
```

### 2. Create virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Start MongoDB
Make sure MongoDB is running locally:
```bash
mongod
```

---

## ▶️ Usage

### 1. Store frames from a video
Put any sample video in the project folder (e.g., `sample.mp4`), then run:
```bash
python store_utils.py sample.mp4
```
This will save frames (every 60th frame by default) into MongoDB.

---

### 2. Fetch and dump frames
To dump stored frames back into a folder:
```bash
python fetch_utils.py
```
This creates a `frames_out/` folder with all frames as `.jpg` files.

---

## 📦 Dependencies
- [pymongo](https://pypi.org/project/pymongo/) – MongoDB driver  
- [gridfs](https://pymongo.readthedocs.io/en/stable/api/gridfs/) – For storing large binary files  
- [opencv-python](https://pypi.org/project/opencv-python/) – For video frame extraction  

Install with:
```bash
pip install pymongo gridfs opencv-python
```

---

## ✅ Example Output
When storing frames:
```
Saved frame 0 to MongoDB
Saved frame 60 to MongoDB
Saved frame 120 to MongoDB
...
```

When fetching frames:
```
Saved frame_0.jpg to frames_out
Saved frame_60.jpg to frames_out
...
```

---

## 🔮 Possible Extensions
- Rebuild video from stored frames  
- Store extra metadata (timestamp, detected objects, etc.)  
- Expose API with Flask/FastAPI for uploading/downloading videos  

---

👨‍💻 Built as a demo project by **Chaitanya Nirfarake**
