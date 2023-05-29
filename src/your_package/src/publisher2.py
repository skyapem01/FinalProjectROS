#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
def talker1():
    pub = rospy.Publisher('Student_ID', String, queue_size=10)
    rospy.init_node('talker2', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        Student_ID = "6352500056"
        rospy.loginfo(Student_ID)
        pub.publish(Student_ID)
        rate.sleep()


if __name__ == '__main__':
    try:
        talker1()
    except rospy.ROSInterruptException:
        pass
