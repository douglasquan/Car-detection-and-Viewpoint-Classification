import matplotlib.pyplot as plt
from PIL import Image

# Define paths to your images
# Assuming 'results_v5' and 'results_v8' are lists containing the paths to the output images from YOLOv5 and YOLOv8 respectively.
results_v5 = ['yolov5_result_1.png', 'yolov5_result_2.png', 'yolov5_result_3.png', 'yolov5_result_4.png']
results_v8 = ['yolov8_result_1.png', 'yolov8_result_2.png', 'yolov8_result_3.png', 'yolov8_result_4.png']

image_paths = [
   'yolov5_result_3.png', 'yolov5_result_4.png',
    'yolov8_result_3.png', 'yolov8_result_4.png'
]

# Create a figure with subplots in a 2x2 grid
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(20, 10))  # Adjust as needed

# Set titles for columns
axes[0, 0].set_title('YOLOv5 Image 3', fontsize=16)
axes[0, 1].set_title('YOLOv5 Image 4', fontsize=16)
axes[1, 0].set_title('YOLOv8 Image 3', fontsize=16)
axes[1, 1].set_title('YOLOv8 Image 4', fontsize=16)

# Remove the x and y ticks for all plots and set the aspect
for ax in axes.flatten():
    ax.axis('off')

# Load and display each image
for i, ax in enumerate(axes.flatten()):
    img = Image.open(image_paths[i])
    ax.imshow(img)
    ax.set_aspect('auto')

# Adjust layout
plt.subplots_adjust(wspace=0, hspace=0.2)  # No space between images

# Display the plot
plt.show()