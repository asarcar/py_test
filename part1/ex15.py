#!/usr/bin/python3

import sys

# non-standard library imports
from asarcar_package import file_exists

def main():
  if (len(sys.argv)!= 3):
    print("Usage: %s <src_file> <dst_file>"%sys.argv[0])
    sys.exit(1)
  scr, src, dst = sys.argv

  if file_exists(dst):
    print("Dst File %s already exists: aborting copy operation"%dst)
    sys.exit(0)
  elif file_exists(src) == False:
    print("Src File %s does not exists: aborting copy operation"%scr)
    sys.exit(0)

  ip_obj = open(src, "r")
  ftxt = ip_obj.read()
  ip_obj.close()

  op_obj = open(dst, "w")
  op_obj.write(ftxt)
  op_obj.close()

  print("%s: copied content from %s to %s"%(scr, src, dst))
  return

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
