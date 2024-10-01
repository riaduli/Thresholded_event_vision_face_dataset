import subprocess

commands = [
    {
        "threshold": "4",
        "metrics_command": "./darknet detector map data/obj_thresh-4_test.data cfg/aff-yolov4.cfg backup/aff-yolov4-4_last.weights",
        "inference_command": "./darknet detector test data/obj_thresh-4.data cfg/aff-yolov4.cfg backup/aff-yolov4-4_last.weights data/threshold_4/*.png"
    },
    {
        "threshold": "8",
        "metrics_command": "./darknet detector map dataobj_thresh-8_test.data cfg/aff-yolov4.cfg backup/aff-yolov4-8_last.weights",
        "inference_command": "./darknet detector test data/obj_thresh-8.data cfg/aff-yolov4.cfg backup/aff-yolov4-8_last.weights data/threshold_8/*.png"
    },
    {
        "threshold": "12",
        "metrics_command": "./darknet detector map data/obj_thresh-12_test.data cfg/aff-yolov4.cfg backup/aff-yolov4-12_last.weights",
        "inference_command": "./darknet detector test data/obj_thresh-12.data cfg/aff-yolov4.cfg backup/aff-yolov4-12_last.weights data/threshold_12/*.png"
    },
    {
        "threshold": "16",
        "metrics_command": "./darknet detector map data/obj_thresh-16_test.data cfg/aff-yolov4.cfg backup/aff-yolov4-16_last.weights",
        "inference_command": "./darknet detector test data/obj_thresh-16.data cfg/aff-yolov4.cfg backup/aff-yolov4-16_last.weights data/threshold_16/*.png"
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
    
    # UNCOMMENT TO RECEIVE METRICS FROM EACH THRESHOLD (ENTIRE DATASET)
    
    # Step 1: Gather metrics
    #print(f"Gathering metrics from threshold_{threshold}....")
    #output = run_command(entry["metrics_command"])
    #print(output)
    #print("=" * 80)

    # Step 2: Gather inference
    print(f"Gathering inference from threshold_{threshold}...")
    output = run_command(entry["inference_command"])
    print(output)
    print("=" * 80)

    press_any_key()
    
print(f"Completed yolov4 processes!")

