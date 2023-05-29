#!/usr/bin/env python3
from std_srvs.srv import Empty, EmptyResponse
import rospy
from std_msgs.msg import String

def callback2(data):
    rospy.loginfo(rospy.get_caller_id() + " -  %s  ", data.data)
    

def user_trigger():
    rospy.wait_for_service('trigger')
    try:
        trigger = rospy.ServiceProxy('trigger', Empty)
        print("Please do something.")
        resp1 = trigger()
        rospy.init_node('listener', anonymous=True)
        rospy.Subscriber("Student_ID", String, callback2)
        rospy.spin()
        print("Done")
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)
        
if __name__ == "__main__":
    user_trigger()
    
    
