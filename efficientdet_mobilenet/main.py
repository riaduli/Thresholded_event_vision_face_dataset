'''
Author: Shahmir Rizvi
Date Created: 10/3/2024
Command: python main.py
Description: This script shows the inference time of Mobilenet and Efficientdet models
'''

import tensorflow as tf
import os
import time
from PIL import Image
import numpy as np

# Average Precision and IOU
# Bounding Box on Image

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

def load_image(image_path, image_size):

  input_data = tf.io.gfile.GFile(image_path, 'rb').read()
  image = tf.io.decode_image(input_data, channels=3, dtype=tf.uint8)
  image = tf.image.resize(
      image, image_size, method='bilinear', antialias=True)
  return tf.expand_dims(tf.cast(image, tf.uint8), 0).numpy()

def get_output_efficientdet(image_folder, model):
    image_files = [os.path.join(image_folder, file) for file in os.listdir(image_folder) if file.endswith('.jpg') or file.endswith(".png")]
     # Load the TFLite model in TFLite Interpreter
    interpreter = tf.lite.Interpreter(model_path=model)
    interpreter.allocate_tensors()

    # Get input and output tensors.
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()
    
    timer = 0
    for image_path in image_files:
        image = load_image(image_path, (416, 416))
        start_time = time.time()
        interpreter.set_tensor(input_details[0]['index'], image)
        interpreter.invoke()
        output_data = interpreter.get_tensor(output_details[0]['index'])
        
        end_time = time.time()
        timer += end_time - start_time
    print("\tNumber of Images: ", len(image_files))
    print('\tElapsed Time: ', round(timer, 3), 's')
    print("\tInference Time per Image: ", round(timer/len(image_files), 5), 's')
    print('\tFrames per Second: ', round(len(image_files)/timer, 2), ' fps')

def get_output_mobilenet(image_folder, model):
    interpreter = tf.lite.Interpreter(model)
    my_signature = interpreter.get_signature_runner()

    image_files = [os.path.join(image_folder, file) for file in os.listdir(image_folder) if file.endswith('.jpg') or file.endswith(".png")]
    
    timer = 0
    for image_path in image_files:
        image = Image.open(image_path)
        image = image.resize((416, 416)).convert('RGB')
        image = np.array(image)
        image = image.astype(np.float32)
        image = np.expand_dims(image, axis=0)
        start_time = time.time()
        output = my_signature(input=image)
        end_time = time.time()
        timer += end_time - start_time

    print("\tNumber of Images: ", len(image_files))
    print('\tElapsed Time: ', round(timer, 3), 's')
    print("\tInference Time per Image: ", round(timer/len(image_files), 5), 's')
    print('\tFrames per Second: ', round(len(image_files)/timer, 2), ' fps')
    
print("Efficientdet")
get_output_efficientdet("image_folder", "efficientdet-d0.tflite")
print("Mobilenet")
get_output_mobilenet("image_folder", "mobilenet.tflite")
