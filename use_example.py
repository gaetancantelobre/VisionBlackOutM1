from SSLBLACKOUT.rsk_control_tools import Robot_controller
from SSLBLACKOUT.object_detection_helper import Detected_Object
from ultralytics import YOLO

import rsk
import cv2

CAMERA_SOURCE = 0  # FOR WINDOWS
# CAMERA_SOURCE = 2  # FOR LINUX

path_to_weights = r"/home/twim/Documents/GitHub/VisionBlackOutM1/best_module_weights.pt"
#path_to_weights = r"C:\Users\twim\Documents\GitHub\VisionBlackOutM1\find_ball\last.pt"


model = YOLO(path_to_weights, verbose=False)

cap = cv2.VideoCapture(2)



with rsk.Client(host='127.0.0.1', key='') as client:
    robot = client.robots['green'][1]
    robot_green1 = Robot_controller(robot)
    # Loop through the video frames
    working = 1
    while working: #while the robot hasent completed the task keep running
        # Read a frame from the video
        success, frame = cap.read()
        object_list = []
        if success:
            # Run YOLOv8 inference on the frame
            results = model(frame, verbose=False)            # Get bounding box of detected objects
            boxes = results[0].boxes.xyxy.tolist()
            # get corresponding classes of detected objects
            classes = results[0].boxes.cls.tolist()
            # Iterate through the results
            for box, cls in zip(boxes, classes):
                    object_list.append(Detected_Object(cls, box))
        if(robot_green1.find_ball_and_score(object_list)): #if 1 is return that means the robot has completed its taskand exit the while loop.
            working = 0
            
    print("Goal scored !!!! ")
                 


                
               
                        
            
