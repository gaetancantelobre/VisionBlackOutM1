from ultralytics import YOLO
from ultralytics.models.yolo.detect.predict import DetectionPredictor
import cv2


from vector_calculation import get_object_angle
from rsk_control_tools import robot_stop, shoot
from object_detection_helper import Detected_Object


from time import sleep
import rsk
import math

ball_detected = False
cap = cv2.VideoCapture(2)
ball_detected = False
goal_is_centred = False

# CAMERA_SOURCE = 0 #FOR WINDOWS
CAMERA_SOURCE = 2  # FOR LINUX

path_to_weights = r"/home/twim/Documents/GitHub/VisionBlackOutM1/newest_trining/detect/train3/weights/best.pt"
# path_to_weights = r"C:\Users\twim\Documents\GitHub\VisionBlackOutM1\distance_calculation\best.pt"

model = YOLO(path_to_weights, verbose=False)

cap = cv2.VideoCapture(2)


CORRECTION_SPEED = 0.05  # in m/s

# Open the video file
ball_touched = False
with rsk.Client(host='127.0.0.1', key='') as client:
    robot = client.robots['green'][1]
    robot_stop(robot)
    # Loop through the video frames
    while not ball_touched or not goal_is_centered:
        # Read a frame from the video
        success, frame = cap.read()
        if success:
            # Run YOLOv8 inference on the frame
            results = model(frame, verbose=False)
            annotated_frame = results[0].plot
            # Get bounding box of detected objects
            boxes = results[0].boxes.xyxy.tolist()
            # get corresponding classes of detected objects
            classes = results[0].boxes.cls.tolist()

            goal_is_centered = False

            # Iterate through the results
            for box, cls in zip(boxes, classes):
                if (cls == Detected_Object.BALL):
                    ball = Detected_Object(cls, box)
                    # set boolean
                    ball_detected = True

                if (cls == Detected_Object.GOAL):
                    goal = Detected_Object(cls, box)
                    if (goal.get_center() >= 150 and goal.get_center() <= 450 and goal.get_width() > 200):
                        goal_is_centered = True

                # Display the annotated frame
            cv2.imshow("YOLOv8 Inference", annotated_frame)

            if (not ball_detected):
                robot.control(0., 0, math.radians(30)*-1)
            elif (ball_detected and not ball_touched):
                # gerter
                ball_angle = math.radians(
                    round((ball.get_angle_deg()*-1), 1))*1.4
                mov_vector = (CORRECTION_SPEED, 0, ball_angle)

                if (ball.get_estimated_distance() > 15):
                    robot.control(mov_vector[0], mov_vector[1], mov_vector[2])
                else:
                    ball_touched = 1
                    robot_stop(robot)
                    sleep(1)

            elif (goal_is_centered and ball_touched):
                robot_stop(robot)
                sleep(1)
                shoot(robot)
            elif (not goal_is_centered and ball_touched):
                robot.control(0, CORRECTION_SPEED, math.radians(20))
            # Break the loop if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        else:
            # Break the loop if the end of the video is reached
            break
            print("out")

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()
