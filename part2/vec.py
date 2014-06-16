#!/usr/bin/env python

import math

## Vector Class
#  Implements an 'n' dimensional vector space
#

class Vec:
    """ Class with 'n' dimensional vector """
    
    # Counts total number of vectors of any dimensions """
    TotalVec = 0 

    # List of integers """
    __vlist = []

    def __init__(self, veclist):
        """ Vec: constructor """
        self.__vlist =  veclist
        Vec.TotalVec += 1
    
    def __del__(self):
        """ Vec: destructor """
        Vec.TotalVec -= 1

    def __len__(self):
        """ Vec: returns dimension of vector """
        return len(self.__vlist)
        
    def __str__(self):
        """ Vec: printable string representation of vector """
        return str(self.__vlist)

    def __add__(self, other):
        """ Vec: Adds two vectors if they are of same size else noop """
        if (len(self) != len(other)):
            return None

        return Vec(map(lambda x,y: x+y, self.__vlist, other.__vlist))

    def __sub__(self, other):
        """ Vec: Subtracts two vectors if they are of same size else noop """
        if (len(self) != len(other)):
            return None

        return Vec(map(lambda x,y: x-y, self.__vlist, other.__vlist))


    def __mul__(self, other):
        """ Vec: Dot product of two vectors if they are of same size else noop """
        if (len(self) != len(other)):
            return None

        return Vec(map(lambda x,y: x*y, self.__vlist, other.__vlist))

    def __nonzero__(self):
        """ Vec: V1 == 0 """
        return (self.scalar_sq() != 0)

    def __eq__(self, other):
        """ Vec: V1 == V2 if every element is same """
        if (len(self) != len(other)):
            return False

        return (sum(map(lambda x,y: math.fabs(x - y), self.__vlist, other.__vlist)) == 0)

    def __lt__(self, other):
        """ Vec: V1 < V2 if they are of same size else noop """
        if (len(self) != len(other)):
            return None

        return (self.scalar_sq() < other.scalar_sq())

    def __gt__(self, other):
        """ Vec: V1 > V2 if they are of same size else noop """
        return (self.scalar_sq() > other.scalar_sq())

    def scalar_sq(self):
        """ Vec: |v|^2 returned """
        return sum(map(lambda x,y: x*y, self.__vlist, self.__vlist))

    def abs(self):
        """ Vec: |v| returned """
        return math.sqrt(self.scalar_sq())
        
