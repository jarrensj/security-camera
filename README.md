# security-camera

picamera.py 
Program takes a picture when motion is detected through the pir sensor and takes a picture or records video with the pi camera. It then sends the image or video through simple mail transfer protocol to a recipient's email 

wiring: 
pir to raspberry pi connections:
vcc pin -- 5V on pi
gnd -- gnd on pi 
out -- GPIO pin 4 on pi
