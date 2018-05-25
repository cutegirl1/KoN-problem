#! /usr/bin/env python
# -*- coding: utf-8 -*-
import time
from subprocess import call
import rospy
import roslib
import actionlib
import geometry_msgs
import std_msgs
import math
from geometry_msgs.msg import PoseWithCovarianceStamped, Quaternion
from math import radians, degrees
from actionlib_msgs.msg import *
from speech import play,listen,tts
from datafile import *

# datafile stores the input array - points which robot will be visiting
# tts is the text to speech function defined in the file sppech.py


# checks if the robot is in the vicinity of the current goal
def callback_pose(data):
	x = data.pose.pose.position.x
	y = data.pose.pose.position.y
	global goal_reached,goal_x,goal_y
	dist=math.sqrt((goal_x - x)**2 + (goal_y - y)**2)
	#print(x,y,dist)
	if dist < 0.8:
		goal_reached=True
		#print 'In Vicinity'

def statuscheck(data):
	print(data.status_list)
	#print(data.header.seq)

#function to send the robot to 'position'
def send(position):
	#print('Next_goal: ' ,goal_x,goal_y)
	#print('go to ' ,positions[i])
	global goal_reached
	goal_reached=False
	call(['rostopic', 'pub', str(-1),  '/rosarnl_node/goalname', 'std_msgs/String', position])
	while goal_reached==False:
                continue

def identify(goal_x,goal_y):
	print('Identifying.....')


# robot reaches the goal
# playback
# tts() -text to speech function defined in speech.py file plays the text
def recieve(data,sleeptime):
	#play()
	time.sleep(2)
	tts(data)
	time.sleep(sleeptime)

if __name__=='__main__':
	rospy.init_node("navigation_snippet")
	# loads the map to the rosarnl node
	call(['rosservice' ,'call', '/rosarnl_node/load_map_file' ,'/home/guest/Gaurav/HRI/final_map.map'])

	# localises the robot inside of the map
	call(['rosservice', 'call', '/rosarnl_node/global_localization'])
	
	#Read the current pose topic (constantly recieves the coordinates(event driven) )
	rospy.Subscriber("rosarnl_node/amcl_pose", PoseWithCovarianceStamped, callback_pose)

	#rospy.Subscriber("rosarnl_node/move_base/status", GoalStatusArray, statuscheck)
	for i in range(len(positions)):
		global goal_reached,goal_x,goal_y
		d = pos[positions[i]]
		goal_x = d[0]
		goal_y = d[1]
		
		#send to intermediate goal
		send(positions[i])
		recieve(speak[i],sleeptime[i])
		print('Changing Goal')
		print 'Reached : ', positions[i]
	send('home1')
	tts('Task completed')
