#!/usr/bin/env python3
'''
This file is to learn about class more detail.
'''

# Declare a class
class Student():
    # method
    def sayHi(self):
        print('hi')

# Declare a class with constructor
class Teacher():
    def __init__(self,name,age):
        print('hi,my name is %s' % name,'and age is %d' % age)


# class inherit
class A():
    def sayByA(self):
        print('I come from A.')

class B(A):
    def sayByB(self):
        print('I come from B.')

if __name__ == '__main__':
    # case1
    tom = Student() # init a Student instance 
    tom.sayHi()
    # case2
    kafaka = Teacher('kafaka',23) 
    # case3 
    b = B()
    b.sayByA()
    b.sayByB()

