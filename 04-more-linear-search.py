import random

"""
Given a list of 20 random numbers, print out the index of numbers that are multiple of 3
"""
n = []
for i in range(20):
    n.append(random.randint(0,500))

for index,each_number in enumerate(n):
    if each_number % 7 == 0:
        print(index, each_number)


"""
Given a list of names, print out all the names with length greater than 7
"""

"""
Given a list of numbers, print out all the numbers that are preceded with a negative number.

Example:
n = [-1,4,5,6-7,8,10,12,-1]
Output:
4
8
"""
