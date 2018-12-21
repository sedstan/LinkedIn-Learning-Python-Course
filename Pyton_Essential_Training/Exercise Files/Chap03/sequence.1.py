#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# x = range(5, 50, 5) #start, end, step; range is not mutable
x = {'one': 1, 'two': 2, 'three': 3}
x['three'] = 42

for k, v in x.items():
  print('k: {}, v: {}'.format(k, v))  
# for i in x:
#     print('i is {}'.format(i))

# list is a mutable sequence
