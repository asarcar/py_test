#!/usr/bin/env python

from sys import argv
from os.path import exists

scr, fname = argv

def print_all_file(fobj):
    print fobj.read()

def rewind_file(fobj):
    f.seek(0)

def print_cur_line(line_num, fobj):
    print line_num, fobj.readline(), 

if exists(fname) == False:
    print "Input file %s does not exist - aborting operation" %fname
    exit(0)

f = open(fname, "r")

print "File %s: content" %fname
print_all_file(f)
rewind_file(f)

for line in range(0, 3):
    print_cur_line(line, f)

f.close()
