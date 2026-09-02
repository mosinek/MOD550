""" File testing functions from tools.py with assert"""
import numpy as np
from tools import NestedFunctions

NUM_OF_NESTED = 3
NUM_IN_NESTED = 3

obj_1_lists = [np.random.uniform(1,10,NUM_IN_NESTED).tolist() for _ in range(NUM_IN_NESTED)]
obj_2_dicts = {f"dict_{i}": {f"value_{j}": np.random.uniform(1,10)for j in range(NUM_IN_NESTED)}
               for i in range(NUM_OF_NESTED)}

# since the data is generated randomly i cannot test for specific output,
# so i just check the data type in the nested objects, and that the numerical sum is a float

num_sum = NestedFunctions.list_of_lists(obj_1_lists)
num_sum2 = NestedFunctions.dict_of_dicts(obj_2_dicts)

def test_list_of_lists():
    """Testing function for pytest, checking type"""
    assert isinstance(num_sum,float)
    for _,j in enumerate(obj_1_lists):
        for k in j:
            assert isinstance(k,float)

def test_dict_of_dicts():
    """Testing function for pytest, checking type"""
    assert isinstance(num_sum2,float)
    for _,j in obj_2_dicts.items():
        for _,k in j.items():
            assert isinstance(k,float)
