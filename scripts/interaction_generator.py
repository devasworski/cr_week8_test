#!/usr/bin/env python

import rospy
from cr_week8_test.msg import human_info
from cr_week8_test.msg import object_info
import random

COUNTER = 1

def interaction_generator():
    global COUNTER
    pub1 = rospy.Publisher('human_info_G', human_info, queue_size=1)
    pub2 = rospy.Publisher('object_info_G', object_info, queue_size=1)
    rospy.init_node('interaction_generator', anonymous=True)
    rate = rospy.Rate(0.1)
    while not rospy.is_shutdown():
        hinfo = human_info()
        oinfo = object_info()
        hinfo.id = COUNTER
        oinfo.id = COUNTER
        COUNTER += 1
        oinfo.object_size = random.randint(1,2)
        hinfo.human_expression = random.randint(1,3)
        hinfo.human_action = random.randint(1,3)
        pub1.publish(hinfo)
        pub2.publish(oinfo)
        rate.sleep()

if __name__ == '__main__':
    try:
        interaction_generator()
    except rospy.ROSInterruptException:
        pass
