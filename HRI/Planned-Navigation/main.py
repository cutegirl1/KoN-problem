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
import sys
import random
from exminmax import Tree
from geometry_msgs.msg import PoseWithCovarianceStamped, Quaternion
from math import radians, degrees
from actionlib_msgs.msg import *
from speech import play,listen,tts
from datafile import *
from transition_cal import *


'''def callback_pose(data):
	x = data.pose.pose.position.x
	y = data.pose.pose.position.y
	global goal_reached,goal_x,goal_y
	dist=math.sqrt((goal_x - x)**2 + (goal_y - y)**2)
	#print(x,y,dist)
	if dist < 0.8:
		goal_reached=True
		#print 'In Vicinity'
'''

def send(position):
	print('Next_goal: ' ,goal_x,goal_y)
	return
	global goal_reached
	goal_reached=False
	call(['rostopic', 'pub', str(-1),  '/rosarnl_node/goalname', 'std_msgs/String', position])
	while goal_reached==False:
		continue

def identify(goal_x,goal_y):
	print('Identifying.....')

def recieve():
	return 'yes'
	x = random.randint(0,1)
	if(x==0):
		return 'no'
	else:
		return 'yes'
	time.sleep(5)
	tts('Hello')
	#play()
	time.sleep(2)
	data=listen()
	time.sleep(2)
	return data

if __name__=='__main__':
	'''
	#rospy.init_node("navigation_snippet")
	#call(['rosservice' ,'call', '/rosarnl_node/load_map_file' ,'/home/guest/Gaurav/HRI/final_map.map'])
	#call(['rosservice', 'call', '/rosarnl_node/global_localization'])
	#Read the current pose topic
	#rospy.Subscriber("rosarnl_node/amcl_pose", PoseWithCovarianceStamped, callback_pose)
	#rospy.Subscriber("rosarnl_node/move_base/status", GoalStatusArray, statuscheck
	'''
	#calculate transition cost
	cal_transition()
	h = len(goals)
	k = 6
	root = Tree('mx',None,sys.maxsize,'home1',False)	
	if k<=h:
		print('final score is : ',root.run(k,goals, prob, took, h, adj))
		while k<>0 and h<>0:
		    val = 9999999
		    node = root
		    print('root' , root.name,root.cat)
		    if root.cat=='mx':
		        for child in root.children:
		            if val>child.value:
		                val = child.value
		                node = child
		    if(root.cat=='mx'):
				d = adj[node.name]
				goal_x = d[0]
				goal_y = d[1]
				print('Going to',node.name)
				send(node.name)
				input_sound=recieve()
		    else:
		    	print('----------')
		        #input from robot-If present
		        if input_sound=='yes':
		            node = root.children[0]
		            k = k-1
		            h = h-1
		            print("Took sign of ",node.name)
		        else:
		            node = root.children[1]
		            h =  h-1
		            print(node.name,"is absent")
		    root = node
		send('home1')
		if k<>0:
			print('Task completed. But not enough people')
		else:
			print('Task completed.')
	else:
	    print('Task not possible')
	    #tts('This task is not possible')
