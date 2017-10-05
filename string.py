#!/usr/bin/env python3
'''
This file is to learn about string type more detail.
'''
# Get length
s1 = "hello,world"
print(len(s1))

# Get substring
print(s1[0])
print(s1[0:2])

# format 
print("hi,I love %s" % ("python!"))

''' some helpful string operate functions '''

# upper and lower
s2 = "hi,HI"
print(s2.upper())
print(s2.lower())
# title
s3 = "test,something."
print(s3.title())

# remove blank
s4 = "I love "
s5 = " python."
s6 = " hhh "
print(s4.rstrip()) # right
print(s5.lstrip()) # left
print(s6.strip())  # both right and left

# location
s7 = "a"
s8 = "absccab"
print(s8.index(s7)) # if can not find the the substring then throw ValueError
print(s8.find(s7)) # if can not find the substring then return -1