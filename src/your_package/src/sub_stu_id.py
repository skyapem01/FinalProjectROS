#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def callback2(data):
    rospy.loginfo(rospy.get_caller_id() + " - studentID : %s  (2)", data.data)

def listener():
    rospy.init_node('listener3', anonymous=True)
    rospy.Subscriber("Student_ID", String, callback2)
    rospy.spin()

if __name__ == '__main__':
    listener()

