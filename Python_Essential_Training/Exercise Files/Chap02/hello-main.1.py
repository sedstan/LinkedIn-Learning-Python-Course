#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import platform

def main():
    message()

# indetion affects statment printing order
def message():
    print('This is python version {}'.format(platform.python_version()))
    print('line_2')
    if False:
        print('line3')
    else:
        print('not true')

if __name__ == '__main__': main()
