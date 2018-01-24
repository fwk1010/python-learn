#!/usr/bin/env python3
'''
This file is to learn about io more detail.
'''
import os
from io import StringIO
from io import BytesIO

class TestCase():
    def in_input(self):
        s = input('input a word\n')
        print('You key in', s)

    def in_file(self, file_name, file_path):
        with open(file_path + file_name, 'r') as f:
            f.read()

    def out_print(self, s):
        print(s)

    def out_file(self, file_name, file_path, s):
        with open(file_path + file_name, 'w') as f:
            f.write(s)

class TestStringIOCase():
    # case 5
    def write_to_memory(self,s):
        f = StringIO()
        f.write(s)
        print(f.getvalue())
        f.close()
    # case 6
    def read_in_memory(self):
        f = StringIO('I in memory now!')
        s = f.readline()
        f.close()
        print(s)

class TestBytesIOCase():
    # case 7
    def write(self,s):
        f = BytesIO()
        f.write(s.encode('utf-8'))
        v = f.getvalue()
        f.close()
        print(v)
    # case 8
    def read(self):
        f = BytesIO(b'\xe4\xbd\xa0\xe5\xa5\xbd\xe4\xb8\x96\xe7\x95\x8c')
        s = f.read()
        f.close()
        print()

if __name__ == '__main__':
    current_path =  os.path.abspath('.') + '/'
    test = TestCase()
    # case1
    test.in_input()
    # case2
    test.in_file('hi.py', current_path)
    # case3
    test.out_print('hello,world\n')
    # case4
    test.out_file('outTest.txt', current_path, 'Test emmmm')

    test2 = TestStringIOCase()
    # case5
    test2.write_to_memory('hi,string io.')
    # case6
    test2.read_in_memory()

    test3 = TestBytesIOCase()
    # case7
    test3.write('你好世界')
    # case8
    test3.read()

