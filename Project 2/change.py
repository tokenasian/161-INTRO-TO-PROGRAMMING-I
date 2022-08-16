# Author: Matthew Armstrong
# Date: 6/24/21
# Description: Write a program that asks the user for a (integer) number of cents, from 0 to 99,
# and outputs how many of each type of coin would represent that amount with the fewest total number of coins.
print('Please enter an amount in cents less than a dollar:')
cents = int(input())
Q = 25
D = 10
N = 5
P = 1
print("Your change will be:")
print("Q:", cents // Q)
cents = cents % Q
print("D:", cents // D)
cents = cents % D
print("N:", cents // N)
cents = cents % N
print("P:", cents // P)
cents = cents % P
