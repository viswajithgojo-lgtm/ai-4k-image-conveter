import cv2
import os

video_path = "/vercel/sandbox/uploads/WhatsApp Video 2025-11-16 at 10.12.54.mp4"
output_dir = "/vercel/sandbox/frames"

os.makedirs(output_dir, exist_ok=True)

cap = cv2.VideoCapture(video_path)
fps = cap.get(cv2.CAP_PROP_FPS)
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
duration = total_frames / fps

print(f"Video FPS: {fps}")
print(f"Total Frames: {total_frames}")
print(f"Duration: {duration:.2f} seconds")

# Extract frames at intervals
frame_interval = max(1, total_frames // 15)
frame_count = 0
saved_count = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    if frame_count % frame_interval == 0:
        frame_path = os.path.join(output_dir, f"frame_{saved_count:04d}.jpg")
        cv2.imwrite(frame_path, frame)
        print(f"Saved: {frame_path}")
        saved_count += 1

    frame_count += 1

cap.release()
print(f"\nTotal frames saved: {saved_count}")
