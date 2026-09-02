"""
Code.py imports the Fridge class, matplotlib and numpy,
to execute and plot the result of the two functions from Fridge,
based on the numpy generated lists of temperature and handle_open data
"""
import matplotlib.pyplot as plt
import numpy as np
from tools import Fridge

temp_data = np.random.uniform(1,7,15)
handle_data = np.random.choice(a=[True,False], size = 15)

power_data = Fridge.fridge_management(temp_data,handle_data)
cumul_power_data, cumul_sum = Fridge.total_power_use(power_data)

plt.plot(range(1,len(temp_data)+1), cumul_power_data, color = 'purple')
plt.plot(range(1,len(temp_data)+1),power_data, color = 'purple')
plt.fill_between(range(1,len(temp_data)+1),cumul_power_data, color = 'purple', alpha = 0.5)
plt.fill_between(range(1,len(temp_data)+1),power_data,color = 'purple' ,alpha = 0.5)
plt.grid(alpha = 0.5)
plt.title("Plot of power usage across time")
plt.xlabel("Time [in measurements]")
plt.ylabel("Power usage")
plt.show()
