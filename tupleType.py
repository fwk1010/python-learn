#!/usr/bin/env python3
'''
This file is to learn about tuple type more detail.
'''
t1 = (1,2,3);
print(t1)

# Get length
t2 = ()
t3 = (1,) # It must have a comma when tuple has one element only.
t4 = (1,2,3,4)
print(len(t2))
print(len(t3))
print(len(t4))

# Get value in tuple by index
t5 = (1,3,4,['A','B'])
print("tuple[0]:",t5[0])

# tuple can not change reference
t6 = (1,2,3)
# t6[0] = 1 # TypeError: 'tuple' object does not support item assignment

# two tuple concat
t7 = (1,3)
t8 = (1,4)
t9 = t7 + t8
print(t9)