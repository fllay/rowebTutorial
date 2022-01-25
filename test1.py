data = None

# Describe this function...
def callback(data):
  print(data.data)


from geometry_msgs.msg import Twist
from std_msgs.msg import String
import rospy
import time
rospy.init_node('blocky_node', anonymous=True)
rospy.Subscriber('chatter', String, callback)
while not rospy.is_shutdown():
  rospy.sleep(1)
