#!/usr/bin/env python

#############################
###### Keywords #############
#1. @ decorator: class & fn #
#############################

import sys

def main():
    """ Testing Decorators """

    arg = sys.argv
    print "Arguments: {}".format(arg)

    del arg[0]

    vals = [int(valstr) for valstr in arg]
    
    strvals = str(vals)
    strvalres = double(*vals)
    print "{}{}: {}\n-- Doc: {}".format(double.__name__, vals, strvalres, double.__doc__)

    strvalres = triple(*vals)
    print "{}{}: {}\n-- Doc: {}".format(triple.__class__.__name__, vals, strvalres, triple.__doc__)

# Decorator Function
def fn_trace(func):
    """ Decorator Function Wrapper: Tracing Function Calls """
    def new_func(*args, **kwargs):
        """ Decorator Function: Tracing Function Calls """ 
        print "\nEntering {}{}----".format(func.__name__, args)
        retval = func(*args, **kwargs)
        print "Exiting\n----"
        return retval
    return new_func

@fn_trace
def double(*values):
    """ Doubles the value of all integers in the list """
    print "Function double{}".format(values)
    return [2*i for i in values]

# Decorator Class
class FunctionTracer(object):
    """ Decorator Class: Tracer for functions """
    def __init__(self, func):
        """ Constructor class for decorator """
        self.func = func
        self.__class__.__name__ = func.__name__
        self.__doc__ = func.__doc__
        # self.__dict__.update(func.__dict__)

    def __call__(self, *args, **kwargs):
        """ Invoked whenever the object is called with a function """
        print "\n{}{}--->".format(self.func.__name__, args)
        retval = self.func(*args, **kwargs)
        print "<----"
        return retval

@FunctionTracer
def triple(*values):
    """ Triples the value of all integers in the list """
    print "Function triple{}".format(values)
    return [3*i for i in values]

if __name__ == "__main__":
    main()
