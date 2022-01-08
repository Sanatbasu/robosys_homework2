#!/usr/bin/env python3


#Copyright_Name RyuichiUeda




import rospy
from std_msgs.msg import Int32


rospy.init_node('pub')
pub = rospy.Publisher('count_up', Int32, queue_size=1)  
rate = rospy.Rate(10)                                
pub_str=1
print('Please enter a number')
while not rospy.is_shutdown():
    pub_str= input()
    pub_str = int (pub_str)
    pub.publish(pub_str)
    rate.sleep()
