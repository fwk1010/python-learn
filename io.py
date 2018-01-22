#!/usr/bin/env python3
'''
This file is to learn about io more detail.
'''
import os

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


if __name__ == '__main__':
    current_path =  os.path.abspath('.') + '/';
    test = TestCase()
    # case1
    test.in_input()
    # case2
    test.in_file('hi.py', current_path)
    # case3
    test.out_print('hello,world\n')
    # case4
    test.out_file('outTest.txt', current_path, 'Test emmmm')
