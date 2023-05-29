#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
def talker1():
    pub = rospy.Publisher('fullname', String, queue_size=10)
    rospy.init_node('talker1', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        fullname = "Worawibun Tiyatha"
        rospy.loginfo(fullname)
        pub.publish(fullname)
        rate.sleep()


if __name__ == '__main__':
    try:
        talker1()
    except rospy.ROSInterruptException:
        pass

