# written by Jarren San Jose
# jarrensj.com 

# when motion detected by pir sensor, 
# pi camera will take a picture/record video and email the image/video  

import time
import picamera
import smtplib
from time import sleep
from gpiozero import MotionSensor
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders

fromaddr = "jarren@jarrensj.com"           #sender email 
password = "password"                     #sender email password

toaddr = "jarren@jarrensj.com"            #recipient
subject = "[Pi] Motion Detected"          #subject of the email

msg = MIMEMultipart()
msg['From'] = fromaddr 
msg['To'] = toaddr
msg['Subject'] = subject

camera = picamera.PiCamera()
camera.hflip = True
camera.vflip = True

pir = MotionSensor(4)

while True:
	pir.wait_for_motion()
	filename = "image.jpg"                            #filename
	camera.start_preview()
	sleep(3)
	camera.stop_preview()
	camera.capture(filename)                          #if picture
	#camera.start_recording(filename)                 #if video
	#camera.stop_recording()
        body = "Motion detected."                         #set message
	msg.attach(MIMEText(body, 'plain'))
        attachment = open(filename, "rb")
	part = MIMEBase('application', 'octet-stream')
	part.set_payload((attachment).read())
	encoders.encode_base64(part)
	part.add_header('Content-Disposition', "attachment; filename = %s" % filename)
	msg.attach(part)
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(fromaddr, password) 
	text = msg.as_string() 
	server.sendmail(fromaddr, toaddr, text) 
	server.quit()
	time.sleep(5);

