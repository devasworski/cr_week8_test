#!/usr/bin/env python

from cr_week8_test.srv import predict_robot_expression, predict_robot_expressionResponse
import rospy
from bayesian_belief_networks.ros_utils import *

def fSize(O):
    return 0.5

def fAction(HA):
    return 1.0/3

def fExpression(HE):
    return 1.0/3

def fAll(HE, HA, O, M):
    '''happy'''
    table = dict()
    table['111H'] = 0.8
    table['112H'] = 1.0
    table['121H'] = 0.8
    table['122H'] = 1.0
    table['131H'] = 0.6
    table['132H'] = 0.8
    table['211H'] = 0.0
    table['212H'] = 0.0
    table['221H'] = 0.0
    table['222H'] = 0.1
    table['231H'] = 0.0
    table['232H'] = 0.2
    table['311H'] = 0.7
    table['312H'] = 0.8
    table['321H'] = 0.8
    table['322H'] = 0.9
    table['331H'] = 0.6
    table['332H'] = 0.7

    table['111N'] = 0.0
    table['112N'] = 0.0
    table['121N'] = 0.0
    table['122N'] = 0.0
    table['131N'] = 0.2
    table['132N'] = 0.0
    table['211N'] = 1.0
    table['212N'] = 1.0
    table['221N'] = 0.9
    table['222N'] = 0.8
    table['231N'] = 0.8
    table['232N'] = 0.6
    table['311N'] = 0.0
    table['312N'] = 0.0
    table['321N'] = 0.0
    table['322N'] = 0.0
    table['331N'] = 0.2
    table['332N'] = 0.1

    table['111S'] = 0.2
    table['112S'] = 0.0
    table['121S'] = 0.2
    table['122S'] = 0.0
    table['131S'] = 0.2
    table['132S'] = 0.0
    table['211S'] = 1.0
    table['212S'] = 1.0
    table['221S'] = 0.9
    table['222S'] = 0.8
    table['231S'] = 0.8
    table['232S'] = 0.6
    table['311S'] = 0.0
    table['312S'] = 0.0
    table['321S'] = 0.0
    table['322S'] = 0.0
    table['331S'] = 0.2
    table['332S'] = 0.1
    key = ''+ HE + HA + O + M
    return table[key]


g = ros_build_bbn(fSize,fAction,fExpression,fAll,domains=dict(HE=['1','2','3'],HA=['1','2','3'],O=['1','2'],M=['H','N','S']))

def handle_predict_robot_expression(input):
    global g
    ha = input.human_action
    he = input.human_expression
    o = input.object_size
    
    if(ha == 0 and he == 0 and o == 0):
        q = g.query()
    elif(ha == 0 and he == 0):
        q = g.query(O = str(o))
    elif (ha == 0 and o == 0):
        q = g.query(HE = str(he))
    elif (he == 0 and o == 0):
        q = g.query(HA = str(ha))
    elif(ha == 0):
        q = g.query( O= str(o),HE = str(he))
    elif (he == 0 ):
        q = g.query(O = str(o),HA = str(ha))
    elif (o == 0):
        q = g.query(HE = str(he),HA = str(ha))
    else:
        q = g.query(O = str(o),HE = str(he),HA = str(ha))
    return predict_robot_expressionResponse(p_happy = q.get(('M','H')),p_neutral = q.get(('M','N')),p_sad = q.get(('M','S')))
   
   
if __name__ == "__main__":
    rospy.init_node('rep')
    rospy.Service('predict_robot_expression_sev', predict_robot_expression, handle_predict_robot_expression)
    rospy.spin()