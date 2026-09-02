""" Fridge management function """

import numpy as np

class Fridge():

    """ 
    Fridge object containing functions computing 
    power usage - instantaneous and cumulative 
    """

    @staticmethod
    def fridge_management(temperature, handle_open):
        """
        Function assessing the instantaneous power usage based on temp and door handle values

        Assumptions:
        - temperature variable is a list of random float values in the range [1,7]
        - handle_open variable is a list of booleans, True or False,
        where True means that the door is open and False indicates that it is closed
        - the power usage is judged based on three conditions;
        - power usage starts at 0, and by fulfilling a condition
        power usage increases +1 up to the total power 3
            the 3 conditions:
            - if the current temp is higher than the one recorded earlier
            (if there is one), add +1 to power_usage
            - if the current temp is higher than mean temp, add + 1 to power usage
            - if handle_open = True, add +1 to power usage

        Return: the function delivers a list of all computed 
        instantaneous power usages of the fridge
        """
        power_list = []
        for i,j in enumerate(temperature,start=0):
            power_point = 0
            if power_list:
                if j > temperature[-1]:
                    power_point += 1
            if j > np.mean(temperature):
                power_point += 1
            if handle_open[i] is True:
                power_point += 1
            power_list.append(power_point)
        return power_list

    @staticmethod
    def total_power_use(list_of_power):
        """
        Function creating a list of cumulative power values,
        based on an input of a list of instantaneous power usages

        Returns: a list of cumulative values of power usage
        """
        time_index = []
        cumulative_power = []
        for i,j in enumerate(list_of_power):
            time_index.append(i)
            if not cumulative_power:
                cumulative_power.append(j)
            else:
                cumulative_power.append(cumulative_power[-1] + j)
        return cumulative_power, sum(cumulative_power)
