#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 19:48:58 2017

@author: AlydaHuerta
"""

import ikDrawer
import numpy as np

def thetas3_matrix (size) 
    thetas3=np.matrix([armPosition[2]*np.ones(size)])
    return thetas 3

def CircleTrajectory (y_pos,R,circle_shift):  
    x_pos= -1* sqrt(R^2-(y_pos)^2)+circle_shift
    return x_pos

def MoveArm(path_length,y_0,y_f,R,velocity,circle_shift):
     s=round(path_length)+1  #how many points we're sampling
     y_points=np.linspace(y_0,y_f, num=s)
      for i in range (0,len(y_points)-1)
                      x_points(i)=CircleTrajectory(y_points(i),R,circle_shift)  
    endpoints=np.matrix([[x_points],[y_points],[thetas3_matrix(length(x_points))]])
   
    R=rospy.rate((s*velocity)/path_length) #the rate at which the angles are being published
    
      for i in range (0,len(x_points)-1):
          endpoint=np.matrix([[endpoints(0,i)],[endpoints(1,i)],[endpoints(2,i)]]);
          angles=ikDrawer.ik(endpoint)
          arm.joint1_cmd(angles(0))
          arm.joint2_cmd(angles(1))
          arm.joint3_cmd(andlges(2))
          R.sleep()