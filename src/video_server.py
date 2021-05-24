#! /usr/bin/env python

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2
import sys
import random
from matplotlib import pyplot
import numpy as np


bridge = CvBridge()

class VideoServer():
  def __init__(self):
    self.video_topic_name = "/camera/rgb/image_raw/"
    self.video_topic = rospy.Subscriber(self.video_topic_name, Image, self.video_callback)
    self.rate = 1.0
    self.img_count = 1
    self.start()

  def start(self):
    print("VideoServer started..")

    while not rospy.is_shutdown():
      pass 
      
    return


  def video_callback(self, img):
    print("Received something..")
    print("Image attributes:")
    print("{ width: %d, height: %d, encoding: %s, is_bigendian: %d, step: %d}" % (img.width, img.height, img.encoding, img.is_bigendian, img.step))
    # print(img)
    try:
        # Convert your ROS Image message to OpenCV2
        cv2_img = bridge.imgmsg_to_cv2(img, "bgr8")
    except CvBridgeError, e:
        print(e)
    else:
        # Save your OpenCV2 image as a jpeg 
        cv2.imwrite('/home/francisco/catkin_ws/src/robot_gui_bridge/tmp/%d.jpeg' % (self.img_count), cv2_img)
        self.img_count += 1
    return


if __name__ == '__main__':
  
  #Args : {id, x, y, period, [neighbors]}
  args = rospy.myargv(argv = sys.argv)
  # if (len(args) >= 4):
    
  #   rid = int(args[1])
  #   x = float(args[2])
  #   y = float(args[3])
  #   period = float(args[4])
  #   neighbors = args[5:]
  #   neighbors = map(lambda x: int(x) , neighbors)

  try:
    rospy.init_node('video_server', anonymous = False)
    print("init_node check")
    video_server = VideoServer()
  except rospy.ROSInterruptException:
    pass
  # else:
  #   print("Wrong node arguments..")