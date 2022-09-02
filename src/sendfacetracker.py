#!/usr/bin/python
import rospy
from facetrackerturtul_pckg.msg import coordinate_msg
import cv2
import sys

	
def publisher_fun():
	rospy.init_node("tracker")
	pub = rospy.Publisher("coordinate", coordinate_msg, queue_size=10)
	message = coordinate_msg()
	message.x = 0.0
	message.y = 0.0
	rate = rospy.Rate(10)
	rospy.loginfo("tracking:")
	cascPath = rospy.get_param("cascadepath")#"/home/banafsheh/catkin_ws/src/facetrackerturtul_pckg/src/haarcascade_frontalface_default.xml"
	faceCascade = cv2.CascadeClassifier(cascPath)

	video_capture = cv2.VideoCapture(0)

	while not rospy.is_shutdown():
		# Capture frame-by-frame
		ret, frame = video_capture.read()

		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		faces = faceCascade.detectMultiScale(
			gray,
			scaleFactor=1.1,
			minNeighbors=10,
			minSize=(80, 80),
			flags=cv2.CASCADE_SCALE_IMAGE
		)

		# Draw a rectangle around the faces
		for (x, y, w, h) in faces:
			cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
			message.x = x+w/2
			message.y = y+h/2
		# Display the resulting frame
		cv2.imshow('Video', frame)

		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
		pub.publish(message)
		rate.sleep()
		
	# When everything is done, release the capture
	video_capture.release()
	cv2.destroyAllWindows()
	
	
if __name__ == "__main__":
	publisher_fun()
