#!/usr/bin/env python

import sys
import rospy
from cr_week8_test.msg import perceived_info, robot_info
import random
from cr_week8_test.srv import predict_robot_expression

predict_robot_expression_prox = rospy.ServiceProxy('predict_robot_expression_sev', predict_robot_expression, persistent=True)

def callback(data):
    global predict_robot_expression_prox
    rospy.wait_for_service('predict_robot_expression_sev')
    try:
        resp = predict_robot_expression_prox(human_action = data.human_action, human_expression = data.human_expression, object_size = data.object_size)
        r_info = robot_info()
        r_info.id = data.id
        r_info.p_happy = resp.p_happy
        r_info.p_sad = resp.p_sad
        r_info.p_neutral = resp.p_neutral
        rospy.loginfo(r_info)
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)
        

def listener():
    rospy.init_node('rc', anonymous=True)
    rospy.Subscriber('perceived_info_G', perceived_info, callback,queue_size=1)
    rospy.spin()


if __name__ == '__main__':
    listener()