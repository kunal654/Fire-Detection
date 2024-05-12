import cv2 as cv
from ultralytics import YOLO

def cm_to_feet(cm):
    return cm / 30.48

def check_flame_height(height_cm):
    height_feet = cm_to_feet(height_cm)
    if height_feet == 4:
        print("Perfect heat")
    elif height_feet > 7:
        print("Too high flame but acceptable")
    else:
        print("Too low, requires more heat")

# Initialize YOLO model
model = YOLO('best.pt')

# Open video file
video_path = 'Flame _Video.mp4'
cap = cv.VideoCapture(video_path)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Predict using YOLO on current frame
    results = model.predict(source=frame, conf=0.2)
    boxes = results.xyxy[0]  # Get bounding boxes
    
    for box in boxes:
        x1, y1, x2, y2, _, _ = box
        height_cm = y2 - y1
        print(f'Flame height: {int(height_cm)} cm')
        check_flame_height(height_cm)
    
    # Display annotated frame
    annotated_frame = results.render()
    cv.imshow('Flame Detection', annotated_frame)
    
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture and close windows
cap.release()
cv.destroyAllWindows()
