#!/usr/bin/env python3
'''
This file is to learn about class more detail.
'''

# Declare a class
class Student():
    # method
    def sayHi(self):
        print('hi')


# use
tom = Student() # init a Student instance 
tom.sayHi()


# Declare a class with constructor
class Teacher():
    def __init__(self,name,age):
        print('hi,my name is %s' % name,'and age is %d' % age)

# use
kafaka = Teacher('kafaka',23) 

