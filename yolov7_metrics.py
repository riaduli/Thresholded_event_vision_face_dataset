import subprocess
import os

# Save the current working directory
original_directory = os.getcwd()

# Change to the 'darknet' directory
os.chdir('darknet')

commands = [
    {
        "threshold": "4",
        "inference_command": "./darknet detector test data/obj_thresh-4.data cfg/aff-yolov7.cfg backup/aff-yolov7-4_last.weights data/threshold_4/test/*.png"
    },
    {
        "threshold": "8",
        "inference_command": "./darknet detector test data/obj_thresh-8.data cfg/aff-yolov7.cfg backup/aff-yolov7-8_last.weights data/threshold_8/test/*.png"
    },
    {
        "threshold": "12",
        "inference_command": "./darknet detector test data/obj_thresh-12.data cfg/aff-yolov7.cfg backup/aff-yolov7-12_last.weights data/threshold_12/test/*.png"
    },
    {
        "threshold": "16",
        "inference_command": "./darknet detector test data/obj_thresh-16.data cfg/aff-yolov7.cfg backup/aff-yolov7-16_last.weights data/threshold_16/test/*.png"
    }
]

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error executing command: {command}\n{e.output}"

def press_any_key():
    input("Press 'Enter' to continue...")

for entry in commands:
    threshold = entry["threshold"]
    
    # Step 1: Gather inference
    print(f"Gathering inference from threshold_{threshold}...")
    output = run_command(entry["inference_command"])
    print(output)
    print("=" * 80)

    press_any_key()

# Change back to the original directory
os.chdir(original_directory)

print("Completed yolov7 process!")
