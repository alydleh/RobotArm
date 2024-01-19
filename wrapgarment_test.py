#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 18:54:04 2017

@author: AlydaHuerta
"""
#you need to define the velocity!!!


#open gripper
#have arm wrap around
#close gripper

import arm_class
import inverseKinematics
import TowelAssistance
from me212cv.msg import GlovePos
import std_msgs.msg

arm=arm_class()

rospy.init_node('arm_controller')

# Glove position handler
global glove_inframe, glove_position
glove_sub = rospy.Subscriber('/glove_position',GlovePos, glove_callback)

global task
task_sub = rospy.Subcriber('/command', std_msgs.msg.String, task_callback)

velocity=22.91

while not task=='finished'
 if task=='wrapping garment': #(Wrap towel around human)
    	task='0'
        arm.open_grippper()
        arm.close_gripper()
        TowelAssistance.MoveArm(8*np.pi*,-8,8,8,velocity,23) #plug in velocity of motors

   def glove_callback(glove_data):
    global glove_inframe, glove_position
    glove_inframe = glove_data.view
    glove_psoition = glove_data.pos

def task_callback(dask_data):
    global task
    task = task_data