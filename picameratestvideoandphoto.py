from picamera2.encoders import H264Encoder
from picamera2 import Picamera2, Preview
import time
import cv2
picam2 = Picamera2()
video_config = picam2.create_video_configuration()
picam2.configure(video_config)
encoder = H264Encoder(bitrate=10000000)
output = "test1.h264"
picam2.start_recording(encoder, output)
time.sleep(2)
im = picam2.capture_array()
cv2.imwrite('file1.png', im)
time.sleep(2)
im = picam2.capture_array()
cv2.imwrite('file2.png', im)
time.sleep(5)
picam2.stop_recording()
