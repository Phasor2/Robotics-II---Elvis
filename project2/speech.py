#!/usr/bin/env python

import rospy
import wave
import os
import sys
from subprocess import Popen
from std_msgs.msg import Int32
from std_msgs.msg import String
from playsound import playsound
# generate random integer values
from random import seed
from random import randint

#arm = rospy.Publisher('/arm_act', Int32, queue_size=1)
#lines shared with dim
path="/home/myturtlebot/catkin_ws/src/speakbot/line/"
done_move=0
result=0
def callback_done_move(data):
	global done_move
	done_move=data.data
	lineCallback()
def callback_result(data):
	global result
	result=data.data
	lineCallback()
def lineCallback():
	global done_move, result,path
	#sharedLines = [0,0]
	#line = data.data
	line = data.data
	if result==1:
		result=0
		playsound(path+"Win.mp3")
	elif result==1:
		result=0
		playsound(path+"Lost.mp3")
	elif result==3:
		result=0
		playsound(path+"Tie.mp3")
	elif done_move!=0 and result==0:
		done_move=0
		value = randint(0, 5)
		playsound(path+str(value)+".mp3"
#rospy.init_node('speak_node')
#rospy.Subscriber("/lines",Int32,lineCallback)
#rospy.Subscriber("/done_move",Int32,callback_done_move)
#rospy.Subscriber("/result",Int32,callback_result)
#rospy.spin()

