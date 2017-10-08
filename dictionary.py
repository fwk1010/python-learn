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

# Get value by get method
d4 = {"a":"apple","b":"banana"}
print("a:%s"%(d4.get("a")))

# modified a dict
d5 = {"name":"jerry","job":"CEO"}
print("%s'job is %s before"%(d5['name'],d5['job']))
d5['job'] = "staff"
print("%s'job is %s later"%(d5['name'],d5['job']))