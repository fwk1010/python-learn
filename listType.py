#!/usr/bin/env python3
'''
This file is to learn about list type more detail.
'''
l1 = [1,'2',5.5]
print(l1)

# Get length
l2 = [1,3,43,5]
print(len(l2))

# Get sub list
print("l2[0]:",l2[0:1])
print("l2[0:2]:",l2[0:2])

# Get element value in list by index
print("l2 of frist vaule:",l2[0])
print("l2 of last value:",l2[-1])

# Change element value in list
l3 = [1,3,2,35,5]
print("change before:",l3)
l3[1] = -1
print("change after:",l3)

# append to list
l4 = [1]
l4.append('23')
print(l4)

# insert into list
l4 = [3,2,1]
l4.insert(0,-1)
print(l4)

# extend to list
l4 = [0,1]
l5 = [2,3,4,5]
l4.extend(l5) # return None
print("extend to list:",l4)

# delete one element in list by index
l5 = [1,2,3]
del l5[1]
print(l5)

# pop
l6 = [1,2,3,4]
l6.pop()
print(l6)

# pop one element in list by index
l7 = [1,3,4,5]
l7.pop(0) # return the remove value
print(l7)

# remove element in list by value 
l8 = [1,2,3]
l8.remove(3) # return None
print(l8)

# sort.It will change original values.
l9 = ['b','a','z','x']
print("sort before:",l9)
l9.sort()
print("sort after:",l9);
# sorted.It will not change original values.
l10 = [1,4,5,3,2]
print(sorted(l10))
print(l10)

# reverse the list
l11 = [1,2,3,4,5]
l11.reverse(); # return None
print(l11)