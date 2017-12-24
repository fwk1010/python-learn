#!/usr/bin/env python3
'''
This file is to learn about function more detail.
'''
# define a function
def func(s):
    print(s)

# use function
func('hi,function!')

# define a function with default parameters
def func_default_paramters(name,age=18,country='China'):
    print('name:%s'%name,'age:%d'%age,'country:%s'%country)

# examples
func_default_paramters('Hanmeimei')
func_default_paramters('Lilei',19)
func_default_paramters('Tom',country='USA')