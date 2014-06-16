#!/usr/bin/env python

from sys import argv

scr, usr = argv
prompt = '> '

print "Hi %s: running script %s" %(usr, scr), " - would like to ask few Qs"
like = raw_input("Do you like me? " + prompt)
live = raw_input("Where do you live?" + prompt)
comp = raw_input("Kind of computer you own?" + prompt)

print "You said like: %r; live %r; comp %r" %(like, live, comp)
