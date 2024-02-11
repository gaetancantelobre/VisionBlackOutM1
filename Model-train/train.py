from ultralytics import YOLO
model = YOLO('yolov8n.yaml').load('yolov8n.pt') # Load model and weights 
results = model.train(data='config.yaml', epochs=20, imgsz='640')  # Train 20 epochs


