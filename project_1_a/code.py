""" File importing and testing the function tools.py"""
import numpy as np
from tools import NestedFunctions

NUM_OF_NESTED = 3
NUM_IN_NESTED = 3

obj_1_lists = [np.random.uniform(1,10,NUM_IN_NESTED).tolist() for _ in range(NUM_IN_NESTED)]
obj_2_dicts = {f"dict_{i}": {f"value_{j}": np.random.uniform(1,10)for j in range(NUM_IN_NESTED)}
               for i in range(NUM_OF_NESTED)}

NestedFunctions.list_of_lists(obj_1_lists)
NestedFunctions.dict_of_dicts(obj_2_dicts)
