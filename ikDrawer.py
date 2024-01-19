#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 10:55:52 2017

@author: AlydaHuerta
"""

#Inverse Kinematics Code

#bring in vector of the endpoint we need to go to

import math

l1=14.02
l2=14.06
l3=5.305
homePosition=[10,0,0]

#The following code calculates a path the robot can take to go to the home position
def getArrayToGoHome
	#Read in current armPosition
	armPosition= #However to look up arm position
	largestDist=abs(homePosition[0]-armPosition[0])
	if abs(homePosition[1]-armPosition[1])>largestDist
    	largestDist=abs(homePosition[1]-armPosition[1])
	largestDist=int(round(largestDist))
	if largestDist<1
    	largestDist=1
	for i in range (0,largestDist-1)
    	endpointPos[i,0]=(homePosition[0]-armPosition[0])/largestDist*(i+1)+armPosition[0]
    	endpointPos[i,1]=(homePosition[1]-armPosition[1])/largestDist*(i+1)+armPosition[1]
    	endpointPos[i,2]=(homePosition[2]-armPosition[2])/largestDist*(i+1)+armPosition[2]
	return endpointPos



#The following code calculates a path from the home position to the drawer handle
def toDrawerfromHome (handleLocation)
	#Read in current armPosition
	armPosition= #However to look up arm position
	distance=abs(handleLocation[0]-armPosition[0])
	distance=int(round(distance))
	for i in (0, distance-1)
		endpointPosHandle[i,0]=(handleLocation[0]-armPosition[0])/distance*(i+1)+armPosition[0]
    	endpointPosHandle[i,1]=(handleLocation[1]-armPosition[1])/distance*(i+1)+armPosition[1]
    	endpointPosHandle[i,2]=(handleLocation[2]-armPosition[2])/distance*(i+1)+armPosition[2]
    return endpointPosHandle



#The following code finds the angles needed in the link to go to the endpoint
def ik(endpointPos)
	Xc=endpointPos[0]-l3*math.cos(endpointPos[2])
	Yc=endpointPos[1]-l3*math.sin(endpointPos[2])
	r=sqrt(Xc^2+Yc^2)
	alpha=math.atan(Yc/Xc)
	gamma=math.acos((-l2^2+l1^2+r^2)/(2*l1*r))
	beta=math.acos((-r^2+l1^2+l2^2)/(2*l1*l2))
	angleOne=alpha+gamma
	angleTwo=-math.pi+beta
	angleThree=endpointPos[2]-angleOne-angleTwo
	anglesToReturn=[angleOne, angleTwo, angleThree]
	return anglesToReturn