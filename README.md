# color_detect
Red Object Detection and Direction Guidance using OpenCV
This Python project uses OpenCV and imutils to detect red-colored objects in real-time via webcam. Based on the position and size of the detected object, it also gives basic direction instructions like Left, Right, Front, or Stop.

**Features**
Live webcam video capture using OpenCV
HSV color space masking for robust re color detection
Noise reduction using Gaussian blur, erosion, and dilation
Circle and center marking for detected objects
Direction detection based on object position and size
Saves detected frames to the captures/ folder with timestam

**Logic Behind Direction Control**

Left: Red object is detected on the left side of the frame
Right: Red object is on the right side
Front: Object is centered but not too close
Stop: Object is too close (radius too large)
**Requirments**

sudo apt update
sudo apt install python3 python3-pip
pip3 install opencv-python imutils

**Sample Output**

Circle drawn around red object
Center marked
Frame saved when a valid red object is detected
