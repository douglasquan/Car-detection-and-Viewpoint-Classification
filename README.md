
# Autonomous Driving: Car Detection and Viewpoint Classification 

## Overview

This repository contains the implementation of car detection and viewpoint classification modules designed to enhance autonomous driving technologies. These components leverage deep learning models to accurately identify vehicles and classify their orientations, improving situational awareness for autonomous systems.

## Car Detection

The car detection module utilizes YOLOv5 and YOLOv8 models, renowned for their efficiency and accuracy in real-time object detection. This module processes images from the KITTI dataset to detect vehicles in various urban driving scenarios.
Features

- Real-time vehicle detection.
- Integration with YOLOv5 and YOLOv8 models for high accuracy.
- Performance optimization for dynamic urban environments.


[YOLOV5 Result](https://youtu.be/TIHbHYUT2AU?si=-MreVkjEw1OpXqYc)
[YOLOV8 Result](https://youtu.be/QrtF-zzVeI0?si=FZ901SWQ9f1_15GP)

## Car Viewpoint Classification

This module classifies the viewpoint of detected vehicles using transfer learning techniques, leveraging the capabilities of pre-trained models such as ResNet50, InceptionV3, and VGG16.
Features

- Accurate viewpoint classification of detected vehicles.
- Uses pre-trained models to enhance learning efficiency.
- Handles diverse and complex traffic scenarios effectively.

### Model Comparison and Selection

To identify the most effective model for viewpoint classification, I compared three leading pre-trained models: ResNet50, InceptionV3, and VGG16. Each model was evaluated based on its accuracy, computational efficiency, and adaptability to the specific task of viewpoint classification. This comparison allowed us to select the best model based on performance metrics specific to our use case, ensuring optimal results.

### Data Preparation

The dataset was meticulously prepared to train the viewpoint classification module. Here are the key steps taken in the data preparation process:

- Data Collection: Utilized images from the KITTI dataset, which provides a variety of annotated images of vehicles in different traffic scenarios.
- Data Preprocessing: Images were resized and normalized to fit the input requirements of each pre-trained model. This standardization ensures that the models can effectively learn from and adapt to the dataset.
- Data Augmentation: To increase the robustness of the model and to simulate a wider range of driving conditions, the dataset was augmented using techniques such as random rotations, horizontal flips, and brightness adjustments. These transformations help the model generalize better across different lighting and environmental conditions.
- Training/Test Split: The prepared dataset was divided into training and testing sets, ensuring that the model can be evaluated on unseen data, thus providing insights into its real-world applicability.

## Insights and Contributions

The project illustrates the effective use of modern object detection and machine learning techniques in practical scenarios. It demonstrates the power of YOLO models in real-time detection and the adaptability of transfer learning for classification tasks. The insights gained from this project include:

- Enhanced understanding of real-time data processing in autonomous systems.
- Practical application of convolutional neural networks in vehicle detection.
- Improved techniques for integrating machine learning models with autonomous driving technologies.

