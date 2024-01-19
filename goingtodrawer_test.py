#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 18:48:23 2017

@author: AlydaHuerta
"""
## right now we use "glove_position" and "task" and "globe_inframe"
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

while not task=='finished':

  if task== 'going to drawer': #Go to Drawer
    	task='0'
    	arm.open_gripper() #open gripper
    	homeMatrix=ikDrawer.getArrayToGoHome() #Gets matrix of motor angles as steps to the home position
    	rowsAndColumns=homeMatrix.size #finds how many rows and columns in the matrix
    	for i in range (0, rowsAndColumns[0]-1): #calls inverse kinematics function for each row of the matrix
    		angleVector=ikDrawer.ik(homeVector[i,:])
    		arm.joint1_cmd(angleVector[0])
    		arm.joint2_cmd(angleVector[1])
    		arm.joint3_cmd(angleVector[2]) #change to joint1_cmd
    	#Now the arm has moved from whatever position it was originally in to the home position
        #this calls upon the ikDrawer class and the arm_class (within the ik_drawer class)
    
    	handleLocation=(26.8,0,0)
    	toHandleMatrix=ikDrawer.toDrawerFromHome(handleLocation) #Gets matrix of motor angles as steps to the handle
    	rowsAndColumns=toHandleMatrix.size #finds how many rows and columns in the matrix
    	for i in range (0, rowsAndColumns[0]-1): #calls inverse kinematics function for each row of the matrix
    		angleVector=ikDrawer.ik(toHandleMatrix[i,:]) 
    		arm.joint1_cmd(angleVector[0])
    		arm.joint2_cmd(angleVector[1])
    		arm.joint3_cmd(angleVector[2])
    	#Now the gripper is at the handle
    	arm.close_gripper() #Close the gripper around the handle
        
#26.8 inches in x direction

# Have arm open gripper
#have arm go to handle
#have arm close gripper
#have arm pull back 

 def glove_callback(glove_data):
    global glove_inframe, glove_position
    glove_inframe = glove_data.view
    glove_psoition = glove_data.pos

def task_callback(dask_data):
    global task
    task = task_data
 