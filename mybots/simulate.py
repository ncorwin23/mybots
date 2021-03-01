import pybullet as p
import pyrosim.pyrosim as pyrosim
import pybullet_data
import time
import numpy as np

FRAMES = 1000 #iterations of loop

physicsClient = p.connect(p.GUI)

p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)

planeId = p.loadURDF("plane.urdf")
bodyID = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate("body.urdf")

backLegSensorValues = np.zeros(FRAMES)
frontLegSensorValues = np.zeros(FRAMES)
for i in range(FRAMES):
	p.stepSimulation()
	backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Back_Leg")
	frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Front_Leg")
	pyrosim.Set_Motor_For_Joint(bodyIndex = robot,jointName = "Torso_Back_Leg",controlMode = "p.POSITION_CONTROL",targetPosition = 0.0,maxForce = 500)
	pyrosim.Set_Motor_For_Joint(bodyIndex = robot,jointName = "Torso_Front_Leg",controlMode = "p.POSITION_CONTROL",targetPosition = 0.0,maxForce = 500)
	time.sleep(1/60)

with open('mybots/data/backLegSensorValueData.npy', 'wb') as file:
    np.save(file, backLegSensorValues)

with open('mybots/data/frontLegSensorValueData.npy', 'wb') as file:
    np.save(file, frontLegSensorValues)

p.disconnect()

print(backLegSensorValues)
print(frontLegSensorValues)
