'''
Author: Shahmir Rizvi, Joey Mulé
Date Created: 10/6/2024
Command: python mobilenet.py || python3 mobilenet.py
Description: This script draws a bounding box for the Mobilenet model
'''

import tensorflow as tf
from PIL import Image
import numpy as np
import os
import cv2
import sys

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Load MobileNet interpreter and signature runner
interpreter = tf.lite.Interpreter("efficientdet_mobilenet/mobilenet.tflite")
my_signature = interpreter.get_signature_runner()

def get_output(image_folder):
    # Collect all image files (JPG and PNG)
    image_files = [os.path.join(image_folder, file) for file in os.listdir(image_folder) if file.endswith('.jpg') or file.endswith(".png")]

    # Ensure there are images in the folder
    if len(image_files) == 0:
        print("No images found in the folder.")
        return
    
    for idx, image_path in enumerate(image_files):
        print(f"\nProcessing image {idx+1}/{len(image_files)}: {image_path}")

        # Load and preprocess the image
        image = Image.open(image_path)
        image = image.resize((416, 416)).convert('RGB')
        image = np.array(image)
        image = image.astype(np.float32) / 255.0  # Normalize input to [0, 1]
        image = np.expand_dims(image, axis=0)

        # Run the model and obtain the output
        output_data = my_signature(input=image)
        print(f"Model output for image {idx+1}: {output_data}")
        if 'output_3' not in output_data:
            print(f"Warning: 'output_3' key not found in output. Available keys: {output_data.keys()}")
            continue
        start_point = (int(output_data['output_3'][0][0][1] * 416), int(output_data['output_3'][0][0][0] * 416))
        end_point = (int(output_data['output_3'][0][0][3] * 416), int(output_data['output_3'][0][0][2] * 416))

        # Draw bounding box on the original image
        image_cv = cv2.imread(image_path)
        image_cv = cv2.resize(image_cv, (416, 416))
        color = (0, 255, 0)
        thickness = 2
        cv2.rectangle(image_cv, start_point, end_point, color, thickness)
	print("=" * 80)
        # Display the image with bounding box
        cv2.imshow("Image with Bounding Box", image_cv)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        

get_output("efficientdet_mobilenet/image_folder")

