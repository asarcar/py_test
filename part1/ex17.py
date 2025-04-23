#!/usr/bin/python3

import sys

# non-standard library imports
from asarcar_package import file_exists


def print_all_file(fobj):
  # read the entire file into a string and print it
  print(fobj.read())

def rewind_file(fobj):
  fobj.seek(0)

def print_cur_line(line_num, fobj):
  print("%i: %s"%(line_num, fobj.readline()), end='')

def main():
  if (len(sys.argv) != 2):
    print("Usage: %s <input_file>" % sys.argv[0])
    sys.exit(1)

  # Get the command line arguments
  scr, fname = sys.argv

  if not file_exists(fname):
    print("Input file %s does not exist - aborting operation" %fname)
    sys.exit(0)

  f = open(fname, "r")

  print("File %s: content" %fname)
  print_all_file(f)
  rewind_file(f)

  for line in range(0, 3):
    print_cur_line(line, f)

  f.close()

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()