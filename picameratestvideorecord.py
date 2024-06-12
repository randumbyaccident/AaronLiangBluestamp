from picamera2.encoders import H264Encoder
from picamera2 import Picamera2
import time
picam2 = Picamera2()
video_config = picam2.create_video_configuration()
picam2.configure(video_config)
encoder = H264Encoder(bitrate=10000000)
output = "test.h264"
picam2.start_recording(encoder, output)
#^May be replaced by 
#picam2.start_encoder(encoder, output)
#picam2.start()
time.sleep(10)
picam2.stop_recording()
#^May be replaced by 
#picam2.stop()
#picam2.stop_encoder()