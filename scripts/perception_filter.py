#!/usr/bin/env python
import rospy
from cr_week8_test.msg import human_info
from cr_week8_test.msg import object_info
from cr_week8_test.msg import perceived_info
import random
import message_filters

pub = rospy.Publisher('perceived_info_G', perceived_info, queue_size=1)

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
    rospy.init_node('pf', anonymous=True)
    sub_1 = message_filters.Subscriber('human_info_G', human_info)
    sub_2 = message_filters.Subscriber('object_info_G', object_info)
    ts = message_filters.ApproximateTimeSynchronizer([sub_1, sub_2], 1, 1, allow_headerless=True)
    ts.registerCallback(callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
