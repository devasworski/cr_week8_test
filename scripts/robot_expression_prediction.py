#!/usr/bin/env python

from cr_week8_test.srv import *
import rospy
#from bayesian.bbn import *
from bayesian_belief_networks.ros_utils import *


def fHappy(HE, HA, O):
    '''happy'''
    table = dict()
    table['111'] = 0.8
    table['112'] = 1
    table['121'] = 0.8
    table['122'] = 1
    table['131'] = 0.6
    table['132'] = 0.8
    table['211'] = 0
    table['212'] = 0
    table['221'] = 0
    table['222'] = 0.1
    table['231'] = 0
    table['232'] = 0.2
    table['311'] = 0.7
    table['312'] = 0.8
    table['321'] = 0.8
    table['322'] = 0.9
    table['331'] = 0.6
    table['332'] = 0.7
    key = ''+ HE + HA + O
    return table[key]


def fNeutral(HE, HA, O):
    '''neutral'''
    table = dict()
    table['111'] = 0
    table['112'] = 0
    table['121'] = 0
    table['122'] = 0
    table['131'] = 0.2
    table['132'] = 0
    table['211'] = 1
    table['212'] = 1
    table['221'] = 0.9
    table['222'] = 0.8
    table['231'] = 0.8
    table['232'] = 0.6
    table['311'] = 0
    table['312'] = 0
    table['321'] = 0
    table['322'] = 0
    table['331'] = 0.2
    table['332'] = 0.1
    key = ''+ HE + HA + O
    return table[key]


def fSad(HE, HA, O):
    '''Sad'''
    table = dict()
    table['111'] = 0.2
    table['112'] = 0
    table['121'] = 0.2
    table['122'] = 0
    table['131'] = 0.2
    table['132'] = 0
    table['211'] = 1
    table['212'] = 1
    table['221'] = 0.9
    table['222'] = 0.8
    table['231'] = 0.8
    table['232'] = 0.6
    table['311'] = 0
    table['312'] = 0
    table['321'] = 0
    table['322'] = 0
    table['331'] = 0.2
    table['332'] = 0.1
    key = ''+ HE + HA + O
    return table[key]

def handle_predict_robot_expression(input):
    #g = ros_build_bbn(fHappy, fNeutral, fSad, domains=dict(HE=[1,2,3],HA=[1,2,3],O=[1,2]))
    RESULT = predict_robot_expressionResponse()
    #g.p(HE = input.human_action, HA = input.human_expression, O = input.object_size)
    RESULT.p_happy = 0.1
    RESULT.p_neutral = 0.1
    RESULT.p_sad = 0.1
    return RESULT
   
def predict_robot_expression_server():
    rospy.init_node('rep')
    s = rospy.Service('predict_robot_expression_sev', predict_robot_expression, handle_predict_robot_expression)
    rospy.spin()
   
if __name__ == "__main__":
    predict_robot_expression_server()