#!/usr/bin/env python

'''
says a line if the line exists for the robot.
Then publishes increment to indicate its done.
'''

#import rospy
import wave
import os
import sys
from subprocess import Popen
#from std_msgs.msg import Int32
#from std_msgs.msg import String
from playsound import playsound

#arm = rospy.Publisher('/arm_act', Int32, queue_size=1)
#lines shared with dim


def lineCallback(data):
	#sharedLines = [0,0]
	#line = data.data
	line = data
	if(os.path.isfile("/home/phong/Desktop/Robotic_2/project2/line/"+ str(line) +".mp3")):
		value=1
		#arm.publish(value)
	
		playsound("/home/phong/Desktop/Robotic_2/project2/line/"+ str(line) +".mp3")
		#pros = Popen("ffplay -autoexit -nodisp /home/myturtlebot/catkin_ws/src/einstein/play1/"+ str(line) +".wav", shell=True);
		#pros.wait()
		#if line not shared with dim we publish done, else have dim publish
		#if(line not in sharedLines):
		value=0
		arm.publish(value)
		increment.publish(line)
	return


lineCallback(1)
#
# rospy.init_node("Einstein")
# increment = rospy.Publisher('/increment', Int32, queue_size=1)
# rospy.Subscriber("/lines",Int32,lineCallback)
# rospy.spin()
#
