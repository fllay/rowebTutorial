pub = None


from geometry_msgs.msg import Twist
from std_msgs.msg import String
import rospy
import time
rospy.init_node('blocky_node', anonymous=True)
pub = rospy.Publisher('chatter', String, queue_size=10)

while not rospy.is_shutdown():
  pub.publish('HiHi')
  rospy.sleep(1)
