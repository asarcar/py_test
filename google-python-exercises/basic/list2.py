#!/usr/bin/env python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Additional basic list exercises

# D. Given a list of numbers, return a list where
# all adjacent == elements have been reduced to a single element,
# so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or
# modify the passed in list.
def remove_adjacent(nums):
  # +++your code here+++
  if (nums is None) or (len(nums)<=1): return nums
  prev = nums[0]
  nums2 = []
  nums2.append(prev)
  for num in nums[1:]:
    if num == prev:
      continue
    # we've hit a new number compared to previous ones
    prev = num
    nums2.append(num)
  return nums2


# E. Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. You may modify the passed in lists.
# Ideally, the solution should work in "linear" time, making a single
# pass of both lists.
def linear_merge(list1, list2):
  # +++your code here+++
  if (list1 is None) or (len(list1)<=0): return list2
  if (list2 is None) or (len(list2)<=0): return list1
  
  len_l1 = len(list1)
  len_l2 = len(list2)

  list3 = []
  (i1,i2) = (0,0)

  while (i1 < len_l1) or (i2 < len_l2):
    # list1 or list2 is exhausted - simply add rest of the other list to the final result
    if i1 == len_l1:
      list3.extend(list2[i2:])
      return list3
    if i2 == len_l2:
      list3.extend(list1[i1:])
      return list3
    
    # whichever element is less is added to the final list and we move to the next element
    if list2[i2] < list1[i1]:
      list3.append(list2[i2])
      i2 += 1
      continue
    
    list3.append(list1[i1])
    i1 += 1
  # we are here as we've reached the end of list1 or list2 or both
  # let us add the remaining list
  
  return

# Note: the solution above is kind of cute, but unforunately list.pop(0)
# is not constant time with the standard python list implementation, so
# the above is not strictly linear time.
# An alternate approach uses pop(-1) to remove the endmost elements
# from each list, building a solution list which is backwards.
# Then use reversed() to put the result back in the correct order. That
# solution works in linear time, but is more ugly.


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# Calls the above functions with interesting inputs.
def main():
  print('remove_adjacent')
  test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
  test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
  test(remove_adjacent([]), [])

  print()
  print('linear_merge')
  test(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
  test(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
  test(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
       ['aa', 'aa', 'aa', 'bb', 'bb'])


if __name__ == '__main__':
  main()
