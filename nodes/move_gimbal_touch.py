#!/usr/bin/env python

PKG = 'aribo'

import roslib; roslib.load_manifest(PKG)

import time
from math import pi
from threading import Thread

import rospy
from sensor_msgs.msg import Joy
from std_msgs.msg import Float64
from dynamixel_controllers.srv import *
from dynamixel_msgs.msg import JointState as JointState
from geometry_msgs.msg import Twist

class MoveGimbal():
    def __init__(self):
        self.is_running = True
        self.step_size = 0.001
        self.touch_data = None
	self.teleopTime = time.time()
        
        rospy.init_node('move_gimbal_touch', anonymous=True)
	self.pan_limit = rospy.get_param('/camera_limits/pan')
	self.tilt_limit = rospy.get_param('/camera_limits/tilt')
        rospy.Subscriber('/teleopCam', Twist, self.read_touch_data)

        self.servo_position_pan = rospy.Publisher('/pan_controller/command', Float64)
        self.servo_position_tilt = rospy.Publisher('/tilt_controller/command', Float64)

        self.pan_joint = 0.0
	self.tilt_joint = 0.0

	self.update_freq = rospy.get_param('gvr_bot/updateFreq')

    def read_touch_data(self, data):
        self.touch_data = data
        self.teleopTime = time.time()

    def update_gimbal_position(self):
	rate = rospy.Rate(self.update_freq)
        while self.is_running:
            if not self.touch_data == None and (time.time() - self.teleopTime)<0.2:
		self.pan_joint += 1 * self.touch_data.angular.z * self.step_size
		self.tilt_joint += 1 * self.touch_data.angular.x * self.step_size

	    if self.pan_joint<self.pan_limit['lower']:
		self.pan_joint=self.pan_limit['lower']
            elif self.pan_joint>self.pan_limit['upper']:
		self.pan_joint=self.pan_limit['upper']

	    if self.tilt_joint<self.tilt_limit['lower']:
	       self.tilt_joint=self.tilt_limit['lower']
            elif self.tilt_joint>self.tilt_limit['upper']:
	       self.tilt_joint=self.tilt_limit['upper']

	    self.servo_position_pan.publish(self.pan_joint)
	    self.servo_position_tilt.publish(self.tilt_joint)
            rate.sleep()

if __name__ == '__main__':
    move_gimbal = MoveGimbal()
    t = Thread(target=move_gimbal.update_gimbal_position)
    t.start()
    rospy.spin()
    move_gimbal.alive = False
    t.join()


