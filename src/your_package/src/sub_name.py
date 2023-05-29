#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
def callback1(data):
    rospy.loginfo(rospy.get_caller_id() + " - name : %s  (1)", data.data)
    

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("fullname", String, callback1)
    rospy.spin()

if __name__ == '__main__':
    listener()

