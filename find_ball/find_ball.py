from ultralytics import YOLO
from ultralytics.models.yolo.detect.predict import DetectionPredictor
import cv2

import rsk
import math
import time


def robot_stop(robot):
    robot.control(0., 0., 0.)


def get_direction_vector(ball_position, image_width, fov_degrees, distance):
    # Calculate the angle of the ball relative to the center of the image
    angle_degrees = ((ball_position - image_width / 2) /
                     image_width) * fov_degrees
    angle_radians = math.radians(angle_degrees)

    # Create a direction vector
    direction_vector = [math.sin(angle_radians),
                        math.cos(angle_radians), distance]

    return direction_vector


def get_ball_angle(ball_position, image_width, fov_degrees):
    # Calculate the angle of the ball relative to the center of the image
    angle_degrees = ((ball_position - image_width / 2) /
                     (image_width / 2)) * (fov_degrees / 2)
    return angle_degrees


ball_found = False
cap = cv2.VideoCapture(2)

path_to_weights = r"/home/twim/Documents/GitHub/VisionBlackOutM1/distance_calculation/best.pt"
#path_to_weights = r"C:\Users\twim\Documents\GitHub\VisionBlackOutM1\distance_calculation\best.pt"

model = YOLO(path_to_weights
    , verbose=False)

# Open the video file
ball_touched = False
with rsk.Client(host='127.0.0.1', key='') as client:
    robot = client.robots['green'][1]
    # Loop through the video frames
    while cap.isOpened() and not ball_touched:
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
            ball_position = -1
            # Iterate through the results
            for box, cls, conf in zip(boxes, classes, confidences):
                x1, y1, x2, y2 = box
                thrity_dist = 65
                width = x2-x1

                ball_position = x1 - (width//2)
                print(f"width in pixels ={width}")

                estimated_distance = thrity_dist/width * 30

                print(f"distance = {estimated_distance}")
                confidence = conf
                detected_class = cls
                name = names[int(cls)]
                ball_found = True
                robot_stop(robot)

                # Display the annotated frame
            cv2.imshow("YOLOv8 Inference", annotated_frame)

            if (not boxes):
                ball_found = False

            if (not ball_found):
                robot.control(0., 0., math.radians(20))
            else:
                pos = x1 + (width//2)
                ball_angle_deg = get_ball_angle(pos, 640, 40)
                ball_angle = math.radians(round((ball_angle_deg*-1), 1))*1.4
                print("rad = " + str(ball_angle))
                print("deg = " + str(ball_angle_deg))
                mov_vector = (0.05, ball_angle)

                if (estimated_distance > 15):
                    robot.control(mov_vector[0], 0, mov_vector[1])

                else:
                    print("god it")
                    robot.control(5, 0, 0)
                    time.sleep(.5)
                    ball_touched = 1
                    robot_stop(robot)
                    robot.kick()

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
