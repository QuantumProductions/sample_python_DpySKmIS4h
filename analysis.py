#!/usr/bin/python

import sys

data_path = sys.argv[1]

f = open(data_path, 'r+')

a = int(f.read(3))
print "First data point: "
print a
f.read(1)
b = int(f.read(3))
print "Second data point: "
print b

def professors_method(a, b):
  quantity = a * 100 + (b - 5)
  return quantity


result = professors_method(a, b)
print "Result"
print result

#print result_data_point_a
