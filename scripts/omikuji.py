#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

n = 0

def cb(message):
    print (" Please 7 and Enter to play OMIKUJI \n ")
    global n
    n = message.data
    i = int(input())
    if i==7 and (7-n) == 1:
        print (" 大吉\n ")
    elif i==7 and (7-n) == 2:
        print (" 中吉\n ")
    elif i==7 and (7-n) == 3:
        print (" 吉\n ")
    elif i==7 and (7-n) == 4:
        print (" 小吉\n ")
    elif i==7 and (7-n) == 5:
        print (" 末吉\n ")
    elif i==7 and (7-n) == 6:
        print(" \n\n---- U  N  C  H  I ----\n\n ")
    else:
        print ("  (´・ω・`)  obey the rule..\n. ")


if __name__=='__main__':
    rospy.init_node('omikuji')
    sub = rospy.Subscriber('count_up', Int32, cb)
    pub = rospy.Publisher('omikuji', Int32, queue_size=1)
    rate = rospy.Rate(2)
#    rospy.spin()
    while not rospy.is_shutdown():
#        pub.publish(n)
        rate.sleep()
