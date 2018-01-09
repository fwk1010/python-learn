#!/usr/bin/env python3
'''
This file is to learn about exception more detail.
'''

# test exception cases
class TestCase():
    # case1 ZeroDivisionError: division by zero
    def two_number_divided(self,a,b):
       s = a / b
       return s
    # case2 FileNotFoundError: [Errno 2] No such file or directory: 'a'
    def open_a_none_file(self,name):
       f = open(name,'r')
       f.close()
    # case3 handle execption
    def handle_exception(self,a,b):
        try:
            result = self.two_number_divided(a,b)
        except ZeroDivisionError as e:
            print('exception message:',e)
        else:
            print(result)

if __name__ == '__main__':
    
    test = TestCase()
    # case1
    # test.two_number_divided(1,0) 
    # case2
    # test.open_a_none_file('a')  
    # case3 
    test.handle_exception(5,2)
    test.handle_exception(5,0)

