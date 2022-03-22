#!/usr/bin/env python

import sys
import rospy
from cr_week8_test.msg import perceived_info, robot_info
import random
from cr_week8_test.srv import predict_robot_expression

predict_robot_expression_prox = rospy.ServiceProxy('predict_robot_expression_sev', predict_robot_expression, persistent=True)
pub = rospy.Publisher('RC_Info', robot_info, queue_size=10)   

def callback(data):
    global predict_robot_expression_prox
    global pub
    rospy.wait_for_service('predict_robot_expression_sev')
    try:
        resp = predict_robot_expression_prox(human_action = data.human_action, human_expression = data.human_expression, object_size = data.object_size)
        r_info = robot_info(id = data.id, p_happy = resp.p_happy, p_sad = resp.p_sad, p_neutral = resp.p_neutral)             
        pub.publish(r_info)
        rospy.loginfo(r_info)
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)
        

def listener():
    global r_info
    rospy.init_node('rc', anonymous=True)
    rospy.Subscriber('perceived_info_G', perceived_info, callback,queue_size=10)
    rospy.spin()


if __name__ == '__main__':
    listener()