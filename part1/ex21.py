#!/usr/bin/env python

##
# Tests for loops and lists
#

from sys import argv

def main():
    """ Main function tests for loop and lists """
    scr, num_str = argv

    type_list = ['int', 'str', 'list', 'misc']
    count_list = create_list(1, int(num_str))
    fruit_list = ['apple', 'orange', 'pear']
    misc_list = [[1, 'pennies'], [2, 'dimes'], [3, 'quarters']]
    
    print_list(type_list[0], count_list) 
    print_list(type_list[1], fruit_list)
    print_list(type_list[2], misc_list)

def create_list(min_num, max_num):
    """ Creates a list of integers starting min_num to max_num """
    return [i for i in range(min_num, max_num + 1)]

def print_list(val_type, alist):
    """ Print the list based on type """
    if (val_type == 'int'):
        fmt_str = "%d"
    elif (val_type == 'str'):
        fmt_str = "%s"
    elif (val_type == 'misc'):
        fmt_str = "%r"
    else:
        # val_type is 'list'
        for i in range(len(alist)):
            print_list('misc', alist[i])
        return
        
    print "List: value_type {}: num_elements {}".format(val_type, len(alist))
    for j in range(len(alist)):
        fmt_line = "alist[{}] = ".format(j) + fmt_str%alist[j]
        print fmt_line
                   
if __name__ == "__main__":
    main()
