import cv2
import os

video_path = '/vercel/sandbox/uploads/WhatsApp Video 2025-11-16 at 10.12.54.mp4'
output_dir = '/vercel/sandbox/frames'

# Create output directory
os.makedirs(output_dir, exist_ok=True)

# Open the video file
cap = cv2.VideoCapture(video_path)

# Get video properties
fps = cap.get(cv2.CAP_PROP_FPS)
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
duration = total_frames / fps

print(f"Video FPS: {fps}")
print(f"Total Frames: {total_frames}")
print(f"Duration: {duration:.2f} seconds")

# Extract frames at regular intervals (every 1 second)
frame_interval = int(fps)
frame_count = 0
saved_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    if frame_count % frame_interval == 0:
        output_path = os.path.join(output_dir, f'frame_{saved_count:04d}.jpg')
        cv2.imwrite(output_path, frame)
        print(f"Saved: {output_path}")
        saved_count += 1

    frame_count += 1

cap.release()
print(f"\nTotal frames saved: {saved_count}")
