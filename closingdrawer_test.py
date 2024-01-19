#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 20:04:40 2017

@author: AlydaHuerta
"""

#have arm push back drawer

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

while not task=='finished'
 elif task=='closing drawer':  #We may have to edit this code to be different than the open drawer code since we won't be right around the handle but will be pushing the gripper against the drawer so there may need to be an offset
    	task='0'
    	done=1
        while done==1: 
    		humanMoving= glove_inframe#Listen to human interaction team 
            if humanMoving==0
               arm.close_gripper()
            elif humanMoving==1:
                endpointToMatch=[glove_position,0,0]#Listen to endpointToMatch from Human communication team
    		    angleVector=ikDrawer.ik(endpointToMatch) #Calls inverse kinematics function to match the current hand position
    		    arm.joint1_cmd(angleVector[0])
    		    arm.joint2_cmd(angleVector[1])
    		    arm.joint3_cmd(angleVector[2])
                arm.close_gripper()
            if endpointToMatch[0]>=27:
                done=0
    	arm.open_gripper() #Open gripper
        
        
 def glove_callback(glove_data):
    global glove_inframe, glove_position
    glove_inframe = glove_data.view
    glove_psoition = glove_data.pos

def task_callback(dask_data):
    global task
    task = task_data