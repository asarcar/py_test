#!/usr/bin/python3
# Copyright 2025 Arijit Sarcar.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

import argparse
import os
import sys

"""A tiny Python program to check that file io is working.
Try running this program from the command line like this:
  python flist.py filename
That should print the contents of the file!
"""
def cat_file(fname):
  assert(os.path.isfile(fname))
  fh = open(fname, 'r')
  assert(fh is not None)
  for line in fh:
    print(line,end="")
  fh.close()

def main():
  parser = argparse.ArgumentParser(description="A simple cat file application")
  parser.add_argument("filename", help="The name of the file to process")
  args = parser.parse_args()
  fname = args.filename
  cat_file(fname)

if __name__ == '__main__':
  main()
