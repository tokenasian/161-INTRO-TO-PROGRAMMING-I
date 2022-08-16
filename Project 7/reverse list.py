# Author: Matthew Armstrong
# Date: 7/21/21
# Description: function that takes as a parameter a list
# and reverses the order of the elements in that list
def reverse_list(val):
    """reverse the order of values in the list"""
    list_length = len(val)
    for i in range(int(list_length/2)):
        n = val[i]
        val[i] = val[list_length-i-1]
        val[list_length-i-1] = n
    print(val)
