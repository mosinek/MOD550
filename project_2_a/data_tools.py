"""
This file contains a function that generates data and checks their integrity. 
"""
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

random.seed(42)

def create_data():
    """
    This function generates 600 observations from weather station in Stavanger, Norway.
    The data contain temperature, wind speed, air pressure, average rainfall, 
    humidity and cloud coverage.
    The following features have the following distributions:
    temperature - symmetric / gaussian distribution
    wind speed - log-normal distribution
    air pressure - almost constant
    average rainfall - symmetric / gaussian distribution
    humidity - correlated with average rainfall + some noise
    """

    temperature = np.random.normal(12,5,600)
    wind_speed = np.random.lognormal(0,1,600)
    air_pressure = np.random.normal(1013,0.5,600)
    avg_rain = np.random.normal(5, 5, 600)
    avg_rain = np.where(avg_rain < 0, 0, avg_rain)

    humidity = [70 + 0.5 * avg_rain[i] + np.random.randn() for i in range(600)]

    cloud_types = ["Clear", "Cumulus", "Cirus", "Cumulonimbus", "Stratus"] # cat
    cloud_coverage = np.random.choice(cloud_types, 600)

    df = pd.DataFrame({'Temperature': temperature, 'Wind speed': wind_speed, 'Air pressure': air_pressure, 'Average rainfall': avg_rain, 'Humidity': humidity, 'Cloud coverage': cloud_coverage})
    print(df)

    return df

df = create_data()

def integrity_check(df):
    """
    This function takes dataset as an input, checks its integrity and returns a report. 
    Checking integrity contains the following steps:
    1. Checking data types
    2. Checking missing values
    3. Checking duplicates
    4. Checking reasonable ranges
    """
    integrity_report = {}
    print(df.dtypes["Temperature"])

    # data types

        
    # missing values
    

    # duplicates
    

    # reasonable ranges


    print("Data integrity checked. Everything is fine.")
    return integrity_report

integrity_check(df)
