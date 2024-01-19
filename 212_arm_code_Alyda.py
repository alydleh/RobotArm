# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import ikDrawer
import numpy as np

#1. How to get the gripper from home position to new position
# 2. How to get gripper around the human so it wraps the cloth around

#theta1=shoulder angle, theta2= elbow angle, theta3=wrist angle, theta4=gripper position

#assuming that the human moves so it's between the arm and the drawer
homePosition=[10,0,0]
towel_home_position=[18,-8,0] #it is just moving the arm to the right of the waist of the person 
                                #whose radius is 8 in/units
R=8 #we are estimating the waist of a person to be less than 8in, so we're making our circle 
    #trajectory with a radius of 8 inches/units
def thetas3_matrix (size) #creates a matrix with the needed amount of thetas3  (constant)
    thetas3=np.matrix([armPosition[2]*np.ones(size)])#get the angle of the wrist from current arm position 
    return thetas 3


def CircleTrajectory (y_pos):
    x_pos= -1* sqrt(R^2-(y_pos))^2+R
    return x_pos

    
while (signal!= ERROR):
    #we now want it to move from home position to towel home position, so 
    #it has to travel a quarter circle to the right of the person
    # a quarter circle= distance of (pi/2)*R=(pi/2)*8=4*pi
    if signal=towel_home_position:
      #we will first discretize this path it is going to move in
      # so that there are waypoints and it goes in a quarter circle trajectory
      path_length=(np.pi/2)*R
      y_points=np.linspace(0,-8, num=round(path_length)+1)
      for i in range (0,len(y_points)-1)
                      x_points(i)=CircleTrajectory(y_points(i))
                     
    endpoints=np.matrix([[x_points],[y_points],[thetas3_matrix(length(x_points))]])
    
    s=round(path_length)+1  #how many points we're sampling
    R=rospy.rate((s*velocity)/path_length)
    
      for i in range (0,len(x_points)-1):
          endpoint=np.matrix([[endpoints(0,i)],[endpoints(1,i)],[endpoints(2,i)]]);
          angles=ikDrawer.ik(endpoint)
          arm.joint1_cmd(angles(0))
          arm.joint2_cmd(angles(1))
          arm.joint3_cmd(andlges(2))
          R.sleep()
          
          ################
          #moving the arm defined as a function
def MoveArm(path_length,y_0,y_f,velocity):
     s=round(path_length)+1  #how many points we're sampling
     y_points=np.linspace(y_0,y_f, num=s)
      for i in range (0,len(y_points)-1)
                      x_points(i)=CircleTrajectory(y_points(i))  
    endpoints=np.matrix([[x_points],[y_points],[thetas3_matrix(length(x_points))]])
   
    R=rospy.rate((s*velocity)/path_length) #the rate at which the angles are being published
    
      for i in range (0,len(x_points)-1):
          endpoint=np.matrix([[endpoints(0,i)],[endpoints(1,i)],[endpoints(2,i)]]);
          angles=ikDrawer.ik(endpoint)
          arm.joint1_cmd(angles(0))
          arm.joint2_cmd(angles(1))
          arm.joint3_cmd(andlges(2))
          R.sleep()
    
          
          
          #################
    
        
        
    if (signal=open_gripper):
        #insert Molly's code
    if (signal=close_gripper):
        #insert Molly's code
    if (signal=wrap_towel_around):
        for i=1:x
        theta1=
        theta2=
        theta3=
        theta4=
#inverse kinematics with the equation for half a circle [y=sqrt(r^2-x^2)] with r being the radius of 
        #a person's waist and I have to calculate this into our generalized coordinates
        #radius of a person's waist = 8in (overestimate)
        
        