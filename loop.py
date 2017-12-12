#!/usr/bin/env python3
'''
This file is to learn about loop more detail.
'''
l1 = [1,3,4]
# for in
for item in l1:
    print(item)

# break
l2 = list(range(1,10))
for i in l2:
    print("current value is %d",i)
    if i == 5 :
        print("break loop when i equals 5")
        break

# while
l3 = ["a","b","d"];
i = 0
while i<len(l3):
    print(l3[i])
    i = i + 1 

# continue
l4 = [1,2,3,4,5]
index = 0
for (l,index )in l4 :
    if index == 2:
        continue
    print("current value is %d",index)
    index = index + 1