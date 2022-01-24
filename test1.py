from geometry_msgs.msg import Twist
from std_msgs.msg import String
import rospy
import time
rospy.init_node('blocky_node', anonymous=True)
while not rospy.is_shutdown():
  rospy.sleep(1)
