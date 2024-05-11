import os
import numpy as np
from scipy.io import loadmat
from PIL import Image

# Set up the paths for images and labels
imageDir = './train_angle/image'
labelDir = './train_angle/labels'
targetDir = './train_angle/preprocessed'

# Make sure the target directory exists
os.makedirs(targetDir, exist_ok=True)

# Loop through the label files and organize the images
for labelFile in os.listdir(labelDir):
    if labelFile.endswith('.mat'):
        # Load corresponding label
        mat = loadmat(os.path.join(labelDir, labelFile))
        annotation = mat['annotation'][0]  # Adjust the indexing as per the .mat file structure

        # Get the corresponding image file name and load it
        imageFileName = labelFile.replace('.mat', '.jpg')
        imagePath = os.path.join(imageDir, imageFileName)
        img = Image.open(imagePath)

        # Filter and process each car in the annotation
        for obj in annotation:
            # Extracting class, truncated, and occluded values for each object
            for idx in range(len(obj['class'][0])):
                class_name = obj['class'][0][idx][0]

                # Safely extract truncated and occluded values
                try:
                    truncated_value = float(obj['truncated'][0][idx][0]) if obj['truncated'][0][
                                                                                idx].size > 0 else 1.0  # Default to 1.0 if empty
                    occluded_value = int(obj['occlusion'][0][idx][0]) if obj['occlusion'][0][
                                                                             idx].size > 0 else 3  # Default to 3 if empty
                except Exception as e:
                    print(f"Error processing entry {idx} in {labelFile}: {e}")
                    continue

                if class_name == 'Car' and truncated_value <= 0.3 and occluded_value <= 2:
                    # Crop the car image using bounding box coordinates
                    bbox = obj['bboxes'][idx]
                    carImage = img.crop((bbox[0], bbox[1], bbox[0] + bbox[2], bbox[1] + bbox[3]))

                    # Resize the image to the input size expected by ResNet-50
                    carImage = carImage.resize((224, 224))  # ResNet-50 uses 224x224 input size

                    # Convert orientation to class label
                    orientation = obj['orient'][idx][0]  # Assuming orientation is a scalar
                    classLabel = int(np.mod(np.round(orientation / 30), 12))

                    # Calculate the folder name based on the class label
                    folderName = f"{classLabel * 30}_degrees"

                    # Create a directory for the class if it doesn't exist
                    classDir = os.path.join(targetDir, folderName)
                    os.makedirs(classDir, exist_ok=True)

                    # Save the image to the respective class directory
                    carImage.save(os.path.join(classDir, imageFileName))
