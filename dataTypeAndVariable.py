#!/usr/bin/env python3
# declare variable
v1 = 1
print(v1)
'''
Python was not declaring variable type explicitly.
'''
# integer number
i0 = 100
i1 = 23
print(i0)
print(i0 + i1)
# float number (has no long type in python 3 any more)
f1,f2 = 1.000,2.50
print(f1)
print(f1 + f2)
print("%.3f"%(f1 + f2)) # format output
# complex

# bool
bt = True
bf = False
print(bt)
print(type(bt))

# string
s1 = "hi,string"
print(s1)
print(type(s1))

# List
l1 = [1,2,3]
print(l1)
print(type(l1))

# tuple
t1 = (1,2,3)
print(t1)
print(type(t1))

# dictionary
d1 = {"a":1,"b":"hh"}
print(d1)
print(type(d1))
