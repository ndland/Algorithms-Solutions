#!/bin/env python

""" This is exercise 1.1.3 from the book Alogrithms by Robert Segdewick """

import sys

if(str(sys.argv[1]) == str(sys.argv[2])):
    if(str(sys.argv[1]) == str(sys.argv[3])):
        print 'equal'
    else:
        print 'not equal'
else:
    print 'not equal'
