#!/usr/bin/python
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from facetrackerturtul_pckg.msg import coordinate_msg
import rospy
import math
import time
x = 0
y = 0
theta = 0
xd = 0
yd = 0
thetad = 0

def go_to_goalpose(x_goal, y_goal, velocity_publisher):
    global x, y, theta
    input_start = 0
    output_end = 10
    input_end = 400
    output_start = 0
    #x_goal = output_start + ((output_end - output_start) / (input_end - input_start)) * (x_goal - input_start)    
    #y_goal = output_start + ((output_end - output_start) / (input_end - input_start)) * (y_goal - input_start)
    #x_goal = (500-x_goal)/50
    x_goal = min(10,(500-x_goal)*10/500)
    #y_goal = (500-y_goal)/50
    y_goal = min(10,(500-y_goal)*10/500)    
    velocity_message = Twist()
    rospy.loginfo("going to:"+str(x_goal)+","+ str(y_goal))
    for i in range(10):
        K_linear = 0.5
        distance = abs(math.sqrt((((x_goal - x) ** 2) + ((y_goal - y) ** 2))))

        linear_speed = distance * K_linear

        K_angular = 5.0
        desired_angle_goal = math.atan2(y_goal - y, x_goal-x)
        angular_speed = (desired_angle_goal - theta) * K_angular

        velocity_message.linear.x = linear_speed
        velocity_message.angular.z = angular_speed
	return velocity_message
        

        
def callback_fun(msg):
	global xd, yd, thetad
	xd = round(msg.x, 4)
	yd = round(msg.y, 4)
	#rospy.loginfo("coordinat:"+str(msg.x)+","+ str(msg.y))	
def callback_fun2(msg):
	global x, y, theta
	x = msg.x
	y = msg.y
	theta = msg.theta
	#rospy.loginfo("tutle:"+str(msg.x)+","+ str(msg.y))
def subscriber_fun():
	rospy.init_node("claculator")
	odom_sub = rospy.Subscriber('/turtle1/pose', Pose, callback = callback_fun2)
	subs = rospy.Subscriber("coordinate", coordinate_msg, callback=callback_fun)
	velocity_publisher = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
	rate = rospy.Rate(10)	
	while not rospy.is_shutdown():
		velocity_publisher.publish(go_to_goalpose(xd, yd, velocity_publisher))
		rate.sleep()
		#rospy.spin()
if __name__ == "__main__":
	subscriber_fun()
