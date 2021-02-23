import numpy as np
import matplotlib.pyplot as plt

backLegSensorValues = np.load("mybots/data/backLegSensorValueData.npy")
frontLegSensorValues = np.load("mybots/data/frontLegSensorValueData.npy")



plt.plot(backLegSensorValues)
plt.plot(frontLegSensorValues)
plt.legend(['Back Leg Sensors', 'Front Leg Sensors'])

plt.show()
