#!/usr/bin/env python3
'''
This file is to learn about conditionals.
'''
# if
v1 = 18
if(v1 >= 18):
    print("Congratulation,you are an adult now.")

# if else
# v2 = "apple"
v2 = "iPhone"
if (v2 == "apple"):
    print("Wow,you have an apple!")
else:
    print("Sorry,you may be want to buy an iPhone X.")

# if elseif
v3 = 5
if(v3 < 0):
    print("You get noting.")
elif (v3 > 0 and v3 < 10):
    print("I catch you!%d"%(v3))
else:
    print("I had know anything.")

# not using ( and )
v4 = 'a'
if v4 == 'a':
    print("Oh,cool!")