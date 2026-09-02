""" File contains class containing two functions operating on nested lists and dictionaries """

class NestedFunctions():
    """ Class contains two functions processing nested objects"""

    @staticmethod
    def list_of_lists(lists):
        """ function that takes list of lists as an input and prints the contents of each list"""
        num_sum = 0
        for i,j in enumerate(lists, start=1):
            print(f"This is list numer {i}, and its contents are {j}")
            for k in j:
                if isinstance(k, (int, float)):
                    num_sum += k
        print(f"Total sum of numerical values in lists: {num_sum}")
        return num_sum

    @staticmethod
    def dict_of_dicts(dicts):
        """ function that takes dict of dicts as an input and prints the contents of each dict"""
        num_sum = 0
        for key,value in dicts.items():
            print(f"This is dictionary '{key}', and its contents are {value}")
            for _,svalue in value.items():
                if isinstance(svalue, (int, float)):
                    num_sum += svalue
        print(f"Total sum of numerical values in dictionaries: {num_sum}")
        return num_sum
