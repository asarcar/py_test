#!/usr/bin/env python

from vec import *

def main():
    v1 = Vec([0, 1, 2])
    v2 = Vec([0, 0, 1])
    v3 = Vec([0, 0])

    print "Vectors: v1 {}: v2 {}: v3 {}".format(str(v1), str(v2), str(v3))
    print "v1 + v2 = {}: v1 - v2 = {}: v1 > v2 = {}".format(str(v1+v2), str(v1-v2), str(v1>v2))
    print "v1 == v3 {}: v1 == v1 {}: v3.nonzero() {}".format(str(v1 == v3), str(v1 == v1), str(v3 != 0))
    print "|v1| = {0:.2f}: |v2| = {1:.2f}: |v3| = {2:.2f}".format(v1.abs(), v2.abs(), v3.abs())

if __name__ == '__main__':
    main()

