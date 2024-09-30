import subprocess

def run_model_metrics(Neural_Network):
    model_scripts = {
        "yolov4": "yolov4_metrics.py",
        "yolov7": "yolov7_metrics.py",
        "EfficientDet-b0": "efficientdet_b0_metrics.py",
        "MobileNets-v1": "mobilenets_v1_metrics.py"
    }

    if Neural_Network in model_scripts:
        script_to_run = model_scripts[Neural_Network]
        print(f"Running {script_to_run} for {Neural_Network} model...\n")
        
        try:
            # Run the corresponding Python script directly in the terminal to preserve interactivity
            subprocess.run(f"python3 {script_to_run}", shell=True, check=True)
            
        except subprocess.CalledProcessError as e:
            print(f"Error executing {script_to_run}: {e.output}")
            return False  # Return False if there was an error
    else:
        print("Invalid Neural Network model name. Please try again.\n")
        return False  # Return False for invalid input
    
    return True  # Return True if the script ran successfully

def main():
    while True:
        print("Please choose the neural network model to view the metrics:")
        print("Options: yolov4, yolov7, EfficientDet-b0, MobileNets-v1")
        
        Neural_Network = input("Enter the model name: ").strip()
        
        # Try running the model metrics script
        if run_model_metrics(Neural_Network):
            break  # Exit the loop if the model script ran successfully

if __name__ == "__main__":
    main()

