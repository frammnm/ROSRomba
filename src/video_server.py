#! /usr/bin/env python

import rospy
# from std_msgs.msg import String
# from ex2_rendezvous.srv import gossip_update, gossip_updateResponse
# from ex2_rendezvous.msg import queue_position_plot
import sys
import random


class VideoServer():
  def __init__(self):
    self.video_topic_name = "/camera/rgb/image_raw/"
    self.video_topic = rospy.Subscriber(self.video_topic_name, queue_position_plot, self.video_callback)
    self.start()

  def start(self):
    print("VideoServer started..")
    return


  def video_callback(self):
    print("Received something..")
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