import rospy
import intera_interface
import arm_observation

# Intera docs used: https://rethinkrobotics.github.io/intera_sdk_docs/5.0.4/intera_interface/html/intera_interface.limb.Limb-class.html
def get_joint_angles(limb):
	joint_names = limb.joint_names()

	angles = [limb.joint_angle(name) for name in joint_names]

	return angles

def get_end_effector_position(limb):
	return limb.endpoint_pose()

def get_observations(limb):
	return {'angles': get_joint_angles(limb), 
			'endpoint_pose': get_end_effector_position(limb)}

def arm_observations_server():
	# Initializes and starts node
	rospy.init_node("arm_observations_server")

	# initialize limb 
	limb = intera_interface.Limb(‘right’)

	s = rospy.Service('arm_observations', arm_observation, get_observations)

	# Prevents thread from exiting until node is shutdown
	rospy.spin()

if __name__ == "__main__":
    arm_observations_server()