import os
import cv2

def video_to_images_converter(input_folder, output_folder):
    for file in os.listdir(input_folder):
        if file.endswith(".mp4"):
            video_path = os.path.join(input_folder, file)
            video = cv2.VideoCapture(video_path)
            success, image = video.read()
            count = 0
            while success:
                image_path = os.path.join(output_folder, file.split(".")[0] + "_frame_" + str(count) + ".jpg")
                cv2.imwrite(image_path, image)
                success, image = video.read()
                count += 1
            video.release()
            print(f"{file} has been converted successfully!")
        else:
            print(f"{file} is not a video file!")


input_folder = input("Enter the input folder path: ")
output_folder = input("Enter the output folder path: ")

# call the function
video_to_images_converter(input_folder, output_folder)
            

# to run the script, open your terminal and run the following command:
# python main.py
# The script will prompt you to enter the input and output folder paths. After entering the paths, the script will convert the videos to images and save them in the output folder.
# you need to install openCV library to run the script. You can install it using the following command:
# pip install opencv-contrib-python
            