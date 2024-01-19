#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 10:55:13 2017

@author: AlydaHuerta
"""

#Main code with main functions

#we'll follow the coordinates of the human at a set high speed of motor (constant feedback of new end effector) 
#the motion will be jerky. So we will have to set a while condition so that it doesn't smash into drawer 
#e.g. while it's not greater than the value. Check before you move that it's not at that value.  

import inverseKinematics
import TowelAssistance


#suscriber to be constantly listening to human interaction team

task= #receeive task signal from human interaction team

    #we need to have it constantly checking to make sure there's not an error signal
    if task== 'going to drawer': #Go to Drawer
    	arm.gripperCmd(0) #open gripper
    	homeMatrix=ikDrawer.getArrayToGoHome() #Gets matrix of motor angles as steps to the home position
    	rowsAndColumns=homeMatrix.size #finds how many rows and columns in the matrix
    	for i in range (0, rowsAndColumns[0]-1): #calls inverse kinematics function for each row of the matrix
    		angleVector=ikDrawer.ik(homeVector[i,:])
    		arm.joint1_cmd(angleVector[1])
    		arm.joint2_cmd(angleVector[2])
    		arm.joint3_cmd(angleVector[3]) #change to joint1_cmd
    	#Now the arm has moved from whatever position it was originally in to the home position
    
    
    	handleLocation=#Listen to handleLocation from human communication team
    	toHandleMatrix=ikDrawer.toDrawerFromHome(handleLocation) #Gets matrix of motor angles as steps to the handle
    	rowsAndColumns=toHandleMatrix.size #finds how many rows and columns in the matrix
    	for i in range (0, rowsAndColumns[0]-1): #calls inverse kinematics function for each row of the matrix
    		angleVector=ikDrawer.ik(toHandleMatrix[i,:]) 
    		arm.joint1_cmd(angleVector[1])
    		arm.joint2_cmd(angleVector[2])
    		arm.joint3_cmd(angleVector[3])
    	#Now the gripper is at the handle
    	arm.gripperCmd(1) #Close the gripper around the handle
    
    elif task== 'opening drawer': #(Open Drawer)
        
    	while task==2 #&& it hasn't readched the end effector position:
     humanMoving= #Listen to human interaction team 
         if humanMoving==0:
           pass
        elif humanMoving==1:             
    		endpointToMatch=#Listen to endpointToMatch from Human communication team
    		angleVector=ikDrawer.ik(endpointToMatch) #Calls inverse kinematics function to match the current hand position
    		arm.joint1_cmd(angleVector[1])
    		arm.joint2_cmd(angleVector[2])
    		arm.joint3_cmd(angleVector[3])
    
    elif task=='closing drawer': (Close Drawer) #We may have to edit this code to be different than the open drawer code since we won't be right around the handle but will be pushing the gripper against the drawer so there may need to be an offset
    	while task==3: #Does the task need to be listened to again to check the while loop? Or will it be automatically updated?
    		endpoinitToMatch=#Listen to endpointToMatch from Human communication team
    		angleVector=ikDrawer.ik(endpointToMatch) #Calls inverse kinematics function to match the current hand position
    		arm.joint1_cmd(angleVector[1])
    		arm.joint2_cmd(angleVector[2])
    		arm.joint3_cmd(angleVector[3])
    	arm.gripperCmd(0) #Open gripper
    
    elif task== '': #(Go to position to hold towel)
    #go to home position first
        homeMatrix=ikDrawer.getArrayToGoHome() #Gets matrix of motor angles as steps to the home position
        rowsAndColumns=homeMatrix.size #finds how many rows and columns in the matrix
        for i in range (0, rowsAndColumns[0]-1) #calls inverse kinematics function for each row of the matrix
    		angleVector=ikDrawer.ik(homeVector[i,:])
    		arm.joint1_cmd(angleVector[1])
    		arm.joint2_cmd(angleVector[2])
    		arm.joint3_cmd(angleVector[3])
    
    #go to position to hold towel
        TowelAssistance.MoveArm(4*np.pi*,0,-8,8,velocity,18) #plug in velocity of motors
    
    
    elif task=='closing gripper': #(Close gripper around towel)
    	arm.gripperCmd(1)
        #we need to implement some control here before the next task to keep the gripper closed
    
    elif task=='wrap garment': #(Wrap towel around human)
    TowelAssistance.MoveArm(8*np.pi*,-8,8,8,velocity,18) #plug in velocity of motors
    
    elif task=='opening gripper': #(Open gripper after human has secured towel)
    	arm.gripperCmd(0)
    
    elif task== 'returning home': #(Go to home position) #@Molly: why can't we use the same code here as the one you
                #used in task 1 to go to home position?
    homeMatrix=ikDrawer.getArrayToGoHome() #Gets matrix of motor angles as steps to the home position
    rowsAndColumns=homeMatrix.size #finds how many rows and columns in the matrix
    	for i in range (0, rowsAndColumns[0]-1): #calls inverse kinematics function for each row of the matrix
    		angleVector=ikDrawer.ik(homeVector[i,:])
    		arm.joint1_cmd(angleVector[1])
    		arm.joint2_cmd(angleVector[2])
    		arm.joint3_cmd(angleVector[3])
    else
    	pass
