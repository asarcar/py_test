#!/usr/bin/env python

def print2_1(*args):
    arg1, arg2 = args
    print "arg1: %r; arg2: %r" % (arg1, arg2)

def print2_2(arg1, arg2):
    print "arg1: %r; arg2: %r" % (arg1, arg2)

print2_1("Brad", "Shaw")
print2_2("Brad", "Shaw")
