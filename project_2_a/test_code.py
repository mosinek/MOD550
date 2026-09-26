"""
This file generates data, corrupts them and check their integrity 
using functions from data_tools.py and test_data_tools.py.
"""

import data_tools
import test_data_tools

df = data_tools.create_data()
report = data_tools.integrity_check(df,n_col=6)

df_corrupted = test_data_tools.corrupt_data(df)
report = data_tools.integrity_check(df_corrupted, n_col=6)
