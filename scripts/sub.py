#!/usr/bin/env python3

<<<<<<< HEAD

#Copyright_Name RyuichiUeda

=======
Copyright_Name RyuichiUeda
>>>>>>> refs/remotes/origin/add-license-1

import rospy
from std_msgs.msg import Int32

n = 0
cal=1
buff = 1
floag =0
def cb(message):
    global n
    global cal
    global buff
    global floag
    if floag == 0:
        buff=message.data*1
    n=buff*cal
    floag=0
if __name__ == '__main__':
        rospy.init_node('sub')
        sub = rospy.Subscriber('count_up', Int32, cb)
        pub = rospy.Publisher('count_up', Int32 ,queue_size=1) 
        rate = rospy.Rate(10)
        while not rospy.is_shutdown():
            cal = input()
            cal = int(cal)
            floag = 1
            cb(1)
            print('ans=',n)
            pub.publish(n)
            rate.sleep()
