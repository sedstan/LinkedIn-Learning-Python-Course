#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# Tuples

x = (1, 'two', 3.0, [4, 'four'], 5)
y = [1, 'two', 3.0, [4, 'four'], 5]
print('x is {}'.format(x))
print(id(x[0]))
print(id(y[0]))

if isinstance(y, tuple):
# if x[0] is y[0]: # is checks for identities; == checks for equality
  print('tuple')
elif isinstance(y, list):
  print('list')
else:
  print('nope')
