import pyrosim.pyrosim as pyrosim
import math

#dimensions
length = 1
width = 1
height = 1

#location
x = 0
y = 0
z = 1.5 #should be half of height to be flush with ground

def Create_World():
	pyrosim.Start_SDF("world.sdf")
	pyrosim.Send_Cube(name="Box", pos=[x-5,y+5,z], size=[length,width,height])
	pyrosim.End()

def Create_Robot():
	pyrosim.Start_URDF("body.urdf")
	pyrosim.Send_Cube(name="Torso", pos=[x,y,z],size=[length,width,height])
	pyrosim.Send_Joint(name = "Torso_Front_Leg", parent = "Torso", child = "Front_Leg", type = "revolute", position = "0.5 0.0 1.0")
	pyrosim.Send_Cube(name="Front_Leg", pos=[0.5,0,-0.5],size=[length,width,height])
	pyrosim.Send_Joint(name = "Torso_Back_Leg", parent = "Torso", child = "Back_Leg", type = "revolute", position = "-0.5 0.0 1.0")
	pyrosim.Send_Cube(name="Back_Leg", pos=[-0.5,0,-0.5],size=[length,width,height])
	pyrosim.End()

Create_Robot()
Create_World()
#pyrosim.Send_Cube(name="Box2", pos=[x+1,y,z+1], size=[length,width,height])

