from ultralytics import YOLO
from ultralytics.models.yolo.detect.predict import DetectionPredictor
import cv2
import pygame
import math


pygame.init()


def get_angle_radian(box_center):
    angle = box_center*45/640
    return angle * math.pi / 180


# Set up the display window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("BALLS POSITION")


model = YOLO(r"C:\Users\twim\Documents\GitHub\VisionBlackOutM1\distance_calculation\best.pt",
             verbose=False)  # Define the colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Define the ball properties
ball_radius = 50
robot1_pos = (400, 550)
ball1_pos = (600, 300)
last_pos = (-1, -1)


# Open the video file
cap = cv2.VideoCapture(0)
running = True
# Loop through the video frames
while cap.isOpened() and running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BLACK)

    # Draw the balls
    pygame.draw.circle(screen, RED, robot1_pos, ball_radius)

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
            height = y2-y1

            if (height > width):
                width = height
                y1 = x1

            center_of_box = x1 + width
            # print(f"center of the box = {center_of_box}")
            angle = get_angle_radian(center_of_box)
            estimated_distance = thrity_dist/width * 30
            angle = angle - math.pi + math.pi/3
            # print(f"width in pixels ={width}")
            new_pos = (robot1_pos[0] + ((estimated_distance*10)*math.cos(angle)),
                       robot1_pos[1]+(estimated_distance*10)*math.sin(angle))
            last_pos = new_pos
            pygame.draw.circle(
                screen, BLUE, new_pos, ball_radius)
            print(f"distance = {estimated_distance}")
            confidence = conf
            detected_class = cls
            name = names[int(cls)]
        print(len(boxes))
        print(last_pos)

        if (len(boxes) == 0 and last_pos != (-1, -1)):
            pygame.draw.circle(
                screen, GREEN, last_pos, ball_radius)
        # Display the annotated frame
        cv2.imshow("YOLOv8 Inference", annotated_frame)
        pygame.display.flip()

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # Break the loop if the end of the video is reached
        break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()
pygame.quit()
