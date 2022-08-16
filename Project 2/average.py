# Author: Matthew Armstrong
# Date: 6/22/21
# Description: Write a program that asks the user for five numbers and then prints out the average of those numbers.
print("Please enter five numbers.")
num_1 = float(input())
num_2 = float(input())
num_3 = float(input())
num_4 = float(input())
num_5 = float(input())
sum_result = num_1 + num_2 + num_3 + num_4 + num_5
avg_result = sum_result / 5
print("The average of those numbers is:")
print(avg_result)
