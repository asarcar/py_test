#!/usr/bin/env python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""A tiny Python program to check that Python is working.
Try running this program from the command line like this:
  python hello.py
  python hello.py Alice
That should print:
  Hello World -or- Hello Alice
Try changing the 'Hello' to 'Howdy' and run again.
Once you have that working, you're ready for class -- you can edit
and run Python code; now you just need to learn Python!
"""

import sys

# non-standard library imports
from utils_asarcar import check_lesser

def Hello(name):
  s = "Hello '%s'" %name
  return s

# Define a main() function that prints a little greeting.
def main():
  # Get the name from the command line, using 'World' as a fallback.
  check_lesser(len(sys.argv), 2)
  if len(sys.argv) > 1:
    name = sys.argv[1]
  else:
    name = 'World'
  s = Hello(name)
  print(s)

#
# Invoke hello.py by either (a) installing external packages AND 
# (b) installing your package in your virtual environment OR by 
# setting PYTHONPATH to the directory that holds local packages:
# pip install utils_asarcar
# pip list # verify utils_asarcar is installed
# OR 
# PYTHONPATH=$DIR_PATH_WITH_LOCAL_PACKAGES hello.py

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
