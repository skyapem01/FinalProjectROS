#!/usr/bin/env python3
from std_srvs.srv import Empty, EmptyResponse
import rospy
import time

def Espresso_callback(req):
    rospy.loginfo("Now making Espresso.")
    rospy.loginfo("Wait a min.")
    rospy.loginfo("===============")
    time.sleep(2)
    rospy.loginfo("served.")
    rospy.loginfo("Take your Espresso.")
    rospy.loginfo("===============")
    return EmptyResponse()

def Americano_callback(req):
    rospy.loginfo("Now making Americano.")
    rospy.loginfo("Wait a min.")
    rospy.loginfo("===============")
    time.sleep(2)
    rospy.loginfo("served.")
    rospy.loginfo("Take your Americano.")
    rospy.loginfo("===============")
    return EmptyResponse()

def Mocca_callback(req):
    rospy.loginfo("Now making Mocca.")
    rospy.loginfo("Wait a min.")
    rospy.loginfo("===============")
    time.sleep(2)
    rospy.loginfo("served.")
    rospy.loginfo("Take your Mocca.")
    rospy.loginfo("===============")
    return EmptyResponse()

def Latte_callback(req):
    rospy.loginfo("Now making Latte.")
    rospy.loginfo("Wait a min.")
    rospy.loginfo("===============")
    time.sleep(2)
    rospy.loginfo("served.")
    rospy.loginfo("Take your Latte.")
    rospy.loginfo("===============")
    return EmptyResponse()

def Cappuccino_callback(req):
    rospy.loginfo("Now making Cappuccino.")
    rospy.loginfo("Wait a min.")
    rospy.loginfo("===============")
    time.sleep(2)
    rospy.loginfo("served.")
    rospy.loginfo("Take your Cappuccino.")
    rospy.loginfo("===============")
    return EmptyResponse()

def stop_callback(req):
    rospy.loginfo("Stop!")
    return EmptyResponse()

if __name__ == "__main__":
    rospy.init_node('service_server')

    rospy.Service('Espresso', Empty, Espresso_callback)
    rospy.Service('Americano', Empty, Americano_callback)
    rospy.Service('Mocca', Empty, Mocca_callback)
    rospy.Service('Latte', Empty, Latte_callback) 
    rospy.Service('Cappuccino', Empty, Cappuccino_callback)
    rospy.Service('stop', Empty, stop_callback)
    rospy.loginfo("Service server ready!")
    rospy.spin()