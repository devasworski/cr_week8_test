#!/usr/bin/env python

from cr_week8_test.srv import predict_robot_expression,predict_robot_expressionResponse
import rospy
from bayesian.bbn import *


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
    table['111'] = 
    table['112'] = 
    table['121'] = 
    table['122'] = 
    table['131'] = 
    table['132'] = 
    table['211'] = 
    table['212'] = 
    table['221'] = 
    table['222'] = 
    table['231'] = 
    table['232'] = 
    table['311'] = 
    table['312'] = 
    table['321'] = 
    table['322'] = 
    table['331'] = 
    table['332'] = 
    key = ''+ HE + HA + O
    return table[key]


def fSad(HE, HA, O):
    '''Sad'''
    table = dict()
    table['111'] = 
    table['112'] = 
    table['121'] = 
    table['122'] = 
    table['131'] = 
    table['132'] = 
    table['211'] = 
    table['212'] = 
    table['221'] = 
    table['222'] = 
    table['231'] = 
    table['232'] = 
    table['311'] = 
    table['312'] = 
    table['321'] = 
    table['322'] = 
    table['331'] = 
    table['332'] = 
    key = ''+ HE + HA + O
    return table[key]


if __name__ == '__main__':
    g = build_bbn(fHappy, fNeutral, fSad)
    g.q()
    g.q(P='high')
    g.q(D=True)
    g.q(S=True)
    g.q(C=True, S=True)
    g.q(D=True, S=True)
    rospy.spin()

def handle_predict_robot_expression(input):
    RESULT = predict_robot_expressionResponse()
    RESULT.p_happy = 
    RESULT.p_neutral =
    RESULT.p_sad =
    return RESULT
   
def predict_robot_expression_server():
    rospy.init_node('predict_robot_expression_server')
    s = rospy.Service('predict_robot_expression', predict_robot_expression, handle_predict_robot_expression)
    rospy.spin()
   
if __name__ == "__main__":
    predict_robot_expression_server()