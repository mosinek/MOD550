""" File testing functions from tools.py with assert"""
import numpy as np
from tools import Fridge

temp_data = np.random.uniform(1,7,15)
handle_data = np.random.choice(a=[True,False], size = 15)

power_data = Fridge.fridge_management(temp_data,handle_data)
cumul_power_data,cumul_sum = Fridge.total_power_use(power_data)

# since the data is generated randomly i cannot test for specific output,
# so i just check that the data follows the logic
# i.e. that the inst_power is in [0,3], and the indices in cumul_power are non-decreasing

def test_power_data():
    """Testing function for pytest, checking logic"""
    for i in power_data:
        assert 0 <= i <= 3


def test_cumul_power_data():
    """Testing function for pytest, checking logic"""
    for i in range(2, len(cumul_power_data)):
        assert cumul_power_data[i] >= cumul_power_data[i-1]
