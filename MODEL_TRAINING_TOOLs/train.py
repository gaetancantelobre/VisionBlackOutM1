from ultralytics import YOLO
model = YOLO('yolov8n.yaml').load('yolov8n.pt')  # Load model and weights
# Train 20 epochs
results = model.train(
    data=r'C:\Users\twim\Documents\GitHub\VisionBlackOutM1\Model-train\config.yaml', epochs=20, imgsz=640)
