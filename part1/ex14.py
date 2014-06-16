#!/usr/bin/env python

from sys import argv

scr, fname = argv

target = open(fname, "w")

line1 = raw_input("Line1: ")
line2 = raw_input("Line2: ")
line3 = raw_input("Line3: ")

target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

target.close() 
