import cv2 as cv
from ultralytics import YOLO

def cm_to_feet(cm):
    return cm / 30.48

def check_flame_height(height_cm):
    height_feet = cm_to_feet(height_cm)
    if height_feet == 4 :
        print("Perfect heat")
    elif height_feet > 7:
        print("Too high flame but acceptable")
    else:
        print("Too low, requires more heat")

model = YOLO('best.pt')

img = cv.imread('Flame _Video.mp4')

results = model.predict(source=img,conf=0.2)

boxes = results[0].boxes.data.tolist()
for box in boxes:
    x1, y1, x2, y2 ,_,_ = box
    height = y2 - y1
    print(f'Flame height: {int(height)} cm')
    flame_height_cm = height
    check_flame_height(flame_height_cm)
    
cv.imshow('image', results[0].plot())
cv.waitKey(0)

