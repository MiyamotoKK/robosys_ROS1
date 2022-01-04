#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32
import random

rospy.init_node('count')
pub = rospy.Publisher('count_up', Int32, queue_size=1)
rate = rospy.Rate(2) #0.5pc
n = 0
while not rospy.is_shutdown():
    n = random.randint(1,6)
    pub.publish(n)
    rate.sleep()
