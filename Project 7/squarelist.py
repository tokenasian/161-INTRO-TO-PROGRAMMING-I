# Author: Matthew Armstrong
# Date: 7/19/21
# Description: function that takes a parameter a list of numbers
# and replaces each value with square of that value
def square_list(nums):
    """replaces each value with the square of that value"""
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2
    print(nums)
