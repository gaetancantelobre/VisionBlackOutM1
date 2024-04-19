from ultralytics import YOLO
from ultralytics.models.yolo.detect.predict import DetectionPredictor
import cv2
import os


print(os.getcwd())
# on linux excute this in console : export QT_QPA_PLATFORM=xcb
#path_to_weights = r"C:\Users\twim\Documents\GitHub\VisionBlackOutM1\newest_trining\detect\train3\weights\best.pt" # if on windows
path_to_weights = r"/home/twim/Documents/GitHub/VisionBlackOutM1/newest_trining/detect/train3/weights/best.pt"

model = YOLO(
    path_to_weights, verbose=False)

# Open the video file
cap = cv2.VideoCapture(2)

# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if success:
        # Run YOLOv8 inference on the frame
        results = model(frame, verbose=False)

        # Visualize the results on the frame
        annotated_frame = results[0].plot()
        boxes = results[0].boxes.xyxy.tolist()
        classes = results[0].boxes.cls.tolist()
        names = results[0].names
        confidences = results[0].boxes.conf.tolist()

        # Iterate through the results
        for box, cls, conf in zip(boxes, classes, confidences):
            x1, y1, x2, y2 = box
            thrity_dist = 65
            width = x2-x1
            print(f"width in pixels ={width}")

            estimated_distance = thrity_dist/width * 30

            print(f"distance = {estimated_distance}")
            confidence = conf
            detected_class = cls
            name = names[int(cls)]
            # Display the annotated frame
        cv2.imshow("YOLOv8 Inference", annotated_frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # Break the loop if the end of the video is reached
        break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()
