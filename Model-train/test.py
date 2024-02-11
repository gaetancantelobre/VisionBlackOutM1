
from ultralytics import YOLO

# This is a code that will load the yolo model and start a live feed from the webcam to detect objects in real time.
#remember to change the path to the weights file to the path of the weights file you want to use.
# also remember to change the source to the source you want to use.
# Load YOLO
net = YOLO("runs/detect/train3/weights/best.pt",)

results = net.predict(source="0", show=True)

