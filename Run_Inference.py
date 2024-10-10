'''
Author: Joey Mulé
Date Created: 10/3/2024
Command: python Run_Inference.py || python3 Run_Inference.py
Description: This script runs the parent script to call one model for inferencing
'''

import subprocess

def run_model_metrics(Neural_Network):
    model_scripts = {
        "Yolov4": "darknet/yolov4_inference.py",
        "Yolov7": "darknet/yolov7_inference.py",
        "EfficientDet-b0": "tflite_models/efficientdet.py",
        "MobileNets-v1": "tflite_models/mobilenet.py"
    }

    if Neural_Network in model_scripts:
        script_to_run = model_scripts[Neural_Network]
        print(f"Running {script_to_run} for {Neural_Network} model...\n")
        
        try:
            # Run the corresponding Python script directly in the terminal
            subprocess.run(f"python3 {script_to_run}", shell=True, check=True)
            
        except subprocess.CalledProcessError as e:
            print(f"Error executing {script_to_run}: {e.output}")
            return False
    else:
        print("Invalid Neural Network model name. Please try again.\n")
        return False
    
    return True

def main():
    while True:
        print("Please choose the neural network model to view the metrics (Entry Specific):")
        print("Options: Yolov4, Yolov7, EfficientDet-b0, MobileNets-v1")
        
        Neural_Network = input("Enter the model name: ").strip()
        
        if run_model_metrics(Neural_Network):
            break

if __name__ == "__main__":
    main()
