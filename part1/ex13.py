#!/usr/bin/env python

from sys import argv

scr, filename = argv

txt = open(filename)

print "File: %r" %filename, " ; Content "
print txt.read()
txt.close()
