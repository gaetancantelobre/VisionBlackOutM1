import pygame
from ultralytics import YOLO
from ultralytics.models.yolo.detect.predict import DetectionPredictor
import cv2


from SSLBLACKOUT.object_detection_helper import Detected_Object
from goal_decision import Rect, Ball

#path_to_weights = r"C:\Users\twim\Documents\GitHub\VisionBlackOutM1\find_ball\last.pt"
path_to_weights = r"/home/twim/Documents/GitHub/VisionBlackOutM1/best_module_weights.pt"


model = YOLO(path_to_weights, verbose=False)

cap = cv2.VideoCapture(0)


# Initialize Pygame
pygame.init()

# Set the dimensions of the screen
screen_width = 640
screen_height = 640
font = pygame.font.Font(None, 32)


# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the background color to black
background_color = (0, 0, 0)
screen.fill(background_color)

# Update the display
pygame.display.flip()

running = True
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()
    screen.fill((0, 0, 0))
    object_list = []
    if success:
        # Run YOLOv8 inference on the frame
        results = model(frame, verbose=False)
        # Visualize the results on the frame
        annotated_frame = results[0].plot()
        boxes = results[0].boxes.xyxy.tolist()
        classes = results[0].boxes.cls.tolist()
        names = results[0].names
        confidences = results[0].boxes.conf.tolist()
        for box, cls in zip(boxes, classes):
            print(cls)
            detected = Detected_Object(cls, box)
            detected_class = detected.get_class()
            if (detected_class == "Ball"):
                new_object = Ball(detected.x1, detected.y1,
                                  detected.get_width(), (255, 165, 0))
            elif (detected_class == "Goal"):
                new_object = Rect(detected.x1, detected.y1,
                                  detected.get_width(), detected.get_height(), (255, 0, 255))
            elif (detected_class == "Robot"):
                new_object = Rect(detected.x1, detected.y1,
                                  detected.get_width(), detected.get_height(), (255, 0, 0))
            distance = font.render(
                str(round(detected.get_estimated_distance(), 0)) + " cm", True, (255, 255, 255))
            angle = font.render(
                str(round(detected.get_angle_deg(), 0)) + "°", True, (255, 255, 255))
            obj_type = font.render(
                detected.get_class(), True, (255, 255, 255))
            screen.blit(distance, (detected.x1 +
                        detected.get_width() + 30, detected.y1 + 32))
            screen.blit(angle, (detected.x1 +
                        detected.get_width() + 30, detected.y1 + 65))
            screen.blit(obj_type, (detected.x1 +
                        detected.get_width() + 30, detected.y1 + 98))
            print(detected.get_estimated_distance())

            object_list.append(new_object)
        for obj in object_list:
            obj.draw(screen)
            print("hello")
        pygame.display.flip()
        cv2.imshow("YOLOv8 Inference", annotated_frame)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


# Quit Pygame
pygame.quit()
