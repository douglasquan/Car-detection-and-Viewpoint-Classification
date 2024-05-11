import cv2
import os
import numpy as np


def make_video(images_folder, output_video, fps, size):
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # or 'XVID'
    out = cv2.VideoWriter(output_video, fourcc, fps, size)

    # Sort files by frame number (adjust according to your filename format)
    images = [img for img in os.listdir(images_folder) if img.endswith(".jpg")]
    images.sort(key=lambda x: int(x.split('_')[-1].split('.')[0]))  # Sorts by the numerical part of the filename

    # Loop through sorted images and write to video file
    for image in images:
        img_path = os.path.join(images_folder, image)
        frame = cv2.imread(img_path)
        out.write(frame)  # Write out frame to video

    # Release everything when job is finished
    out.release()



# Example usage
images_folder = '/home/douglas-quan/Documents/CSC420/project2/project2/train/image_left'
output_video = '/home/douglas-quan/Documents/CSC420/project2/project2/video.mp4'
fps = 30  # Frames per second
size = (1920, 1080)  # Size of the frames. Make sure this matches your images.

make_video(images_folder, output_video, fps, size)
