#Question 1

"""A time tuple is the usage of a tuple (list of ordered items/functions) for the ordering and notation of time."""

#Question 2

import datetime,time
print (time.strftime("%I:%M:%S"))


#Question 3

import datetime,time
print ("Month:",time.strftime("%B"))


#Question 4

import datetime,time
print ("Day:",time.strftime("%A"))


#Question 5

import datetime
day=datetime.date(2021,1,11)
print(day.strftime("%A,%d"))


#Question 6

import datetime,time
print(time.asctime(time.localtime()))


#Question 7

import math
from math import factorial
num=int(input("Enter the number: "))
n=factorial(num)
print(n)


#Question 8

import math
from math import gcd
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print(math.gcd(a,b))


#Question 9

import os
print(os.getcwd()) # current working directory
print(os.environ)  #user environment








