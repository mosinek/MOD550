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

def check_data_types_n_columns(df,n_columns):
    """
    This function check data types of the columns and return True if they are correct and False otherwise. 
    """
    # shouldn't we define expected_types since we know the truth about our data? 
    # answer: true! but in the fututre we will have to use this function on unforeseen data, so idk if we can expect it in the function
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns
    numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns
    
    if (len(df.columns) == n_columns):
        shape = True
        print("Number of columns in dataframe matches expectation.")
    else:
        shape = False
        print("The number of columns detected does NOT match expectations!")
        
    if (len(categorical_cols) + len(numerical_cols)) == len(df.columns):
        print("All columns are categorical or numerical!")
        if shape is True:
            return True
        else:
            return False
    elif(len(df.select_dtypes(exclude=['object','category','int64','float64'])).columns) > 0:
        # elif when we add all other data types the number of columns matches!
        print("There are some unforeseen other data types in the data!")
        return False
    # how can we check if the number of columns is what we expect??? we'd need to add nr of columns as a variable,
    # which is chunky, but i guess thats how we have to do it?

def check_missing_values(df):
    """
    This functions checks if there are any missing values in the dataset, returns False if there are any and True otherwise.
    """
    if df.isnull().sum().sum() > 0:
        print("Dataset contains missing values:")
        for col in df.columns:
            missing_values = df[col].isnull().sum()
            if missing_values > 0:
                print(f"Column: {col} contains {missing_values} missing values!")
        return False

    else:
        print("Dataset has no missing values!")
        return True

def check_duplicates(df):
    """
    This function checks if there are any duplicate rows in the dataset. It returns True if there are no duplicates and False otherwise.
    """
    if df.duplicated().sum() == 0:
        print("No duplicate rows detected.")
        return True
     
    else:
        print(f"{df.duplicated().sum()} duplicate rows detected.")
        return False

def check_ranges(df):
    """
    This function check if the ranges of the data are reasonable. For example:
    -humidity should be between 0 and 100,
    -wind speed and average rainfall cannot be negative
    The function returns True if all ranges are OK and False otherwise.
    """
    if ((df["Humidity"] < 0) | (df["Humidity"] > 100)).any():
        print("Humidity column contains values outside the expected range!")
        return False

    if (df["Wind speed"] < 0).any():
        print("Wind speed column contains negative values!")
        return False

    if (df["Average rainfall"] < 0).any():
        print("Average rainfall column contains negative values!")
        return False

    print("All ranges are reasonable.")
    return True

def integrity_check(df,n_col):
    """
    This function takes dataset as an input, checks its integrity and returns a report. 
    Checking integrity contains the following steps:
    1. Checking data types
    2. Checking missing values
    3. Checking duplicates
    4. Checking reasonable ranges
    """
    print(f"-----\nINTEGRITY CHECK:")
    integrity_report = {
        "data_types": check_data_types_n_columns(df,n_col),
        "missing_values": check_missing_values(df),
        "duplicates": check_duplicates(df),
        "ranges": check_ranges(df)
    }

    if all(integrity_report.values()):
        print("Integrity test: OK.")
    else:
        print("Integrity test: FAILED.")

    return integrity_report

integrity_check(df,n_col=6)