#!/usr/bin/env python

import rospy
from cr_week8_test.msg import perceived_info
import random

def callback(hdata, odata):
    global pub
    FILTER = random.randint(1,8)
    p_info = perceived_info()
    p_info.human_action = hdata.human_action if not (FILTER == 2 or FILTER == 4 or FILTER == 6 or FILTER == 7) else 0
    p_info.human_expression = hdata.human_expression if not (FILTER == 3 or FILTER == 5 or FILTER == 6 or FILTER == 7) else 0
    p_info.object_size = odata.object_size if not (FILTER == 1 or FILTER == 4 or FILTER == 5 or FILTER == 7) else 0
    p_info.id = hdata.id
    pub.publish(p_info)

def listener():
    rospy.init_node('filter', anonymous=True)
    rospy.Subscriber('perceived_info_G', perceived_info, callback,queue_size=1)
    rospy.spin()

if __name__ == '__main__':
    listener()
