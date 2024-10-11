# Thresholded_event_vision_face_dataset
all_threshold_15fps.zip

    threshold_4.zip
    	–test: 963 .txt and 963 .png files
    	–train: 6641 .txt and 6641 .png files
      –valid: 2034 .txt and 2034 .png files
    
    threshold_8.zip
    	–test: 963 .txt and 963 .png files
    	–train: 6641 .txt and 6641 .png files
      –valid: 2034 .txt and 2034 .png files
    
    threshold_12.zip
    	–test: 963 .txt and 963 .png files
    	–train: 6641 .txt and 6641 .png files
      –valid: 2034 .txt and 2034 .png files
    
    threshold_16.zip
    	–test: 963 .txt and 963 .png files
    	–train: 6641 .txt and 6641 .png files
      –valid: 2034 .txt and 2034 .png files

# Understanding of file naming and labeling conventions
file name: 105-250_png.rf.2e5cb960eecaae0cd27a8e75f649d461.png

    The prefix "105-250_png" represents the original image file, 
    where "105" indicates the video file (number) and "205" refers to the frame of the video (or timestamp). 
    The suffix, ex: "rf.2e5cb960eecaae0cd27a8e75f649d461" 
    is a unique hash generated by Roboflow upon export to ensure that each file name is distinct (threshold_x).

    Inside of the label file (ex: "105-250_png.rf.2e5cb960eecaae0cd27a8e75f649d461.txt") 
    the 5 values (ex: "0 0.5757211538461539 0.5204326923076923 0.19471153846153846 0.3473557692307692") 
    correspond to respective variables n, x, y, w, h.
    n - class number (0 - person)
    x - normalized x coordinate for the center of the bounding box
    y - normalized y coordinate for the center of the bounding box
    w - normalized width of the bounding box
    h - normalized height of the bounding box

# Citation
Please consider citing our paper:

------------------------------------------------------------------
```bibtex
@misc{islam2024descriptorfacedetectiondataset,
  title={Descriptor: Face Detection Dataset for Programmable Threshold-Based Sparse-Vision}, 
  author={Riadul Islam and Sri Ranga Sai Krishna Tummala and Joey Mulé and Rohith Kankipati and Suraj Jalapally and Dhandeep Challagundla and Chad Howard and Ryan Robucci},
  year={2024},
  eprint={2410.00368},
  archivePrefix={arXiv},
  primaryClass={cs.CV},
  url={https://arxiv.org/abs/2410.00368},
}
```
# Questions
If you have any questions about our dataset or desire any weights of any other models, please contact Dr. Riadul Islam
```bibtex
Email: riaduli@umbc.edu
```



------------------------------------------------------------------
PARENT FILE

'Run_Inference.py'
Run this script after organizing all other model files
------------------------------------------------------------------

!! BEFORE RUNNING ANY CODE !!

Organize directories as follows

------------------------------------------------------------------
YOLOv4 & YOLOv7

1. Clone and setup darknet: https://github.com/pjreddie/darknet

2. Clone files from this github (https://github.com/riaduli/Thresholded_event_vision_face_dataset)

Inside of the darknet folder:

3. Place each folder (per threshold) within 'sample_all_threshold_15fps' INTO 'darknet/data'

MAKE sure all threshold_x folders are placed and within this directory - 'darknet/data'

***BEFORE CONTINUING***

PLACE 'aff-process.py' into 'darknet/data' and RUN the script

This should create a test.txt file within each threshold folder

FOR THE '.weights', '.data', '.names', & '.cfg' FILES

4. Place all 'aff-yolov4-X_last.weights' and 'aff-yolov7-X_last.weights' INTO 'darknet/backup'

5. Place all '.data' files INTO 'darknet/data'

6. Place '.names' file INTO 'darknet/data'

7. Place all '.cfg' files INTO 'darknet/cfg'

***FINAL***

8. Place 'yolov4_inference.py' and 'yolov7_inference.py' INSIDE the 'darknet' folder

MAKE SURE the parent file 'Run_Inference.py' is NOT inside the 'darknet' folder
It SHOULD be one directory back

------------------------------------------------------------------


------------------------------------------------------------------
MOBLINET & EFFICIENT-DET

1. Place the 'efficientdet_mobilnet' folder inside the SAME directory as the parent script 'Run_Inference.py'
2. Done!
------------------------------------------------------------------

