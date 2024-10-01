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

##################
PARENT FILE

'Run_Metrics.py'
##################

!! BEFORE RUNNING ANY CODE !!

Organize directories as follows

##################################################################
YOLOv4 & YOLOv7

1. Clone and setup darknet: https://github.com/pjreddie/darknet

2. Clone files from this github (https://github.com/riaduli/Thresholded_event_vision_face_dataset)

Inside of the darknet folder:

3. Extract each zipped folder (per dataset) within 'all_threshold_15fps.zip' INTO 'darknet/data'

MAKE sure all threshold_x folders are unzipped and within this directory - 'darknet/data'

***BEFORE CONTINUING***
PLACE 'face_dataset-process.py' into 'darknet/data' and RUN the script

This should create a train/valid/test.txt file within each train/valid/test folder of each threshold
***********************

'.weights', '.data', '.names', & '.cfg' files

4. Place all 'aff-yolov4-X_last.weights' and 'aff-yolov7-X_last.weights' INTO 'darknet/backup'

5. Place all '.data' files INTO 'darknet/data'

6. Place '.names' file INTO 'darknet/data'

7. Place all '.cfg' files INTO 'darknet/cfg'

***FINAL***
8. Place 'yolov4_metrics.py' and 'yolov7_metrics.py' INSIDE 'darknet' folder

MAKE SURE the parent file 'Run_Metrics.py' is NOT inside the 'darknet' folder
It SHOULD be one directory back
##################################################################

##################################################################
MOBLINET



##################################################################

##################################################################
EFFICIENT-DET


##################################################################

