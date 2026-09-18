"""
jebany docstring
"""
import numpy as np
import random
import matplotlib.pyplot as plt

random.seed(42)

def create_data():
    """ weather station"""

    temperature = np.random.normal(12,5,600)
    wind_speed = np.random.lognormal(0,1,600)
    air_pressure = np.random.normal(1013,0.5,600)
    avg_rain = np.random.normal(5, 5, 600)
    avg_rain = np.where(avg_rain < 0, 0, avg_rain)

    humidity = [70 + 0.5 * avg_rain[i] + np.random.randn() for i in range(600)]

    cloud_types = ["Clear", "Cumulus", "Cirus", "Cumulonimbus", "Stratus"] # cat
    cloud_coverage = [np.random.choice(cloud_types, 600)]

    plt.scatter(range(600), temperature)
    plt.xlabel("Observation")
    plt.ylabel("Temperature")
    plt.title("Temperature")
    plt.show()

    plt.scatter(range(600), wind_speed)
    plt.xlabel("Observation")
    plt.ylabel("Wind speed")
    plt.title("Wind Speed")
    plt.show()

    plt.scatter(range(600), air_pressure)
    plt.xlabel("Observation")
    plt.ylabel("Air pressure")
    plt.title("Air Pressure")
    plt.show()

    plt.scatter(range(600), avg_rain)
    plt.xlabel("Observation")
    plt.ylabel("Rain")
    plt.title("Average Rainfall")
    plt.show()

    plt.scatter(range(600), humidity)
    plt.xlabel("Observation")
    plt.ylabel("Humidity")
    plt.title("Average Humidity")
    plt.show()

    print(cloud_coverage)


create_data()