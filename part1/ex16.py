#!/usr/bin/python3

import sys

def print2_1(*args):
    print("#args: %i" % len(args))
    i=1
    for arg in args:
      print("arg #%i: %r"%(i, arg))
      i += 1
    print("-----------")
def print2_2(arg1, arg2):
    print("arg1: %r; arg2: %r" % (arg1, arg2))
    print("-----------")

def main():
  if (len(sys.argv) < 3):
    print("Usage: %s <arg1> <arg2> ..." % sys.argv[0])
    sys.exit(1)
  
  print2_1(*sys.argv[1:])
  print2_2(sys.argv[1], sys.argv[2])

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()