#!/usr/bin/env python3
'''
This file is to learn about dictionary type more detail.
'''
# declare a dict
d1 = {"a":1,"b":2}
print(d1)

# Get length
d2 = {"1":1,"2":2,"3":3}
print(len(d2))

# Get value by key
d3 = {"name":"Tom","age":34}
print("name:%s,age:%s"%(d3["name"],d3["age"]))

# Get value by get() method
d4 = {"a":"apple","b":"banana"}
print("a:%s"%(d4.get("a")))

# modified a dict
d5 = {"name":"jerry","job":"CEO"}
print("%s'job is %s before"%(d5['name'],d5['job']))
d5['job'] = "staff"
print("%s'job is %s later"%(d5['name'],d5['job']))

# delete k-v in dict by key
d6 = {"name":"mock","sex":"man"}
print("before:",d6)
del d6['sex']
print("later:",d6)

# delete k-v in dict by pop() method
d7 = {"name":"fly","sex":"man"}
print("before:",d7)
d7.pop('name')
print("later:",d7)

# clear all k-v in dict by clear() method
d8 = {"a":"apple","b":"banna"}
print("before:",d8)
d8.clear()
print("later:",d8)

# delete dict
d9 = {"name":"kupo"}
del d9
# print(d9) # throws NameError: name 'd9' is not defined

# Get all keys by keys() method
d10 = {"a":1,"b":2}
print(d10.keys())

# Get all values by values() method
d10 = {"a":1,"b":2}
print(d10.values())

# Get all k-v by items() method
print(d10.items())

# judge a dict has the key or not by in
print('a' in d10)