#!/usr/bin/env python

from sys import argv
from os.path import exists

scr, src, dst = argv

if exists(dst):
    print "Dst File %s already exists: aborting copy operation" %dst
    exit(0)
elif exists(src) == False:
    print "Src File %s does not exists: aborting copy operation" %scr
    exit(0)

ip_obj = open(src, "r")
ftxt = ip_obj.read()
ip_obj.close()

op_obj = open(dst, "w")
op_obj.write(ftxt)
op_obj.close()

print "%s: copied content from %s to %s" %(scr, src, dst)

exit(0)
