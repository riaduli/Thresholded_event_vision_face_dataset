'''
Author: Shahmir Rizvi, Joey Mulé
Date Created: 10/6/2024
Command: python efficientdet.py || python3 efficientdet.py
Description: This script draws a bounding box for the Efficientdet model
'''

import tensorflow as tf
import os
import cv2
import sys

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

def load_image(image_path, image_size):
    input_data = tf.io.gfile.GFile(image_path, 'rb').read()
    image = tf.io.decode_image(input_data, channels=3, dtype=tf.uint8)
    image = tf.image.resize(image, image_size, method='bilinear', antialias=True)
    return tf.expand_dims(tf.cast(image, tf.uint8), 0).numpy()

def get_output(image_folder, model):
    image_files = [os.path.join(image_folder, file) for file in os.listdir(image_folder) if file.endswith('.jpg') or file.endswith(".png")]
    if len(image_files) == 0:
        print("No images found in the folder.")
        return
    
    # Load the TFLite model in the TFLite Interpreter
    interpreter = tf.lite.Interpreter(model_path=model)
    interpreter.allocate_tensors()

    # Get input and output tensors
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    for idx, image_path in enumerate(image_files):
        print(f"\nProcessing image {idx+1}/{len(image_files)}: {image_path}")

        # Load and preprocess the image
        image = load_image(image_path, (416, 416))
        interpreter.set_tensor(input_details[0]['index'], image)
        interpreter.invoke()

        # Get model output
        output_data = interpreter.get_tensor(output_details[0]['index'])
        print(f"Model output for image {idx+1}: {output_data}")
        start_point = (int(output_data[0][0][2]), int(output_data[0][0][1]))
        end_point = (int(output_data[0][0][4]), int(output_data[0][0][3]))

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


get_output("efficientdet_mobilenet/image_folder", "efficientdet_mobilenet/efficientdet-b0.tflite")


