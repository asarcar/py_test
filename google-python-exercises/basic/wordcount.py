#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import os
import sys

# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

# CONSTANTS
TOPCOUNT      = 20
COUNTWORDS    = '--count'
TOPCOUNTWORDS = '--topcount'

def hash_words(filename):
  """Creates a dictionary of '<word> <count>' with all words lower cased for a given file."""
  assert(os.path.isfile(filename))
  filehandle = open(filename, 'r')
  assert(filehandle is not None)

  word_hash = {}

  for line in filehandle:
    word_list = line.split()
    for word in word_list:
      w = word.lower()
      # increment the count associated with the word in the dictionary
      # if the words does not exist, assume the default value is 0
      word_hash[w] = word_hash.get(w, 0) + 1 
  filehandle.close()
  return word_hash

###
def print_words(filename):
  """Prints one per line '<word> <count>' sorted by word for the given file."""
  word_hash = hash_words(filename)
  sorted_word_counts = sorted(word_hash.items(), key=lambda tuple: tuple[0])
  for (word, count) in sorted_word_counts:
    print(word, count)
  return

###
def print_top(filename):
  """Prints top N words '<word> <count>' sorted by word for the given file."""
  word_hash = hash_words(filename)
  # sort alphabetically and then sort on count - assuming that STABLE sorting
  sorted_word_counts = sorted(word_hash.items(), key=lambda tuple: tuple[0])
  top_word_by_count = sorted(sorted_word_counts, key=lambda tuple: tuple[1], reverse=True)
  N = TOPCOUNT
  top_N_words = top_word_by_count[:N]
  for (word, count) in top_N_words:
    print(word, count)
  return


# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
  if len(sys.argv) != 3:
    print('usage: ./wordcount.py {%s | %s} filename' %(COUNTWORDS, TOPCOUNTWORDS))
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option != COUNTWORDS and option != TOPCOUNTWORDS:
    print('unknown option: ' + option)
    sys.exit(1)

  # option == --count:
  if option == COUNTWORDS:
    print_words(filename)
    return
  
  # option == --topcount:
  print_top(filename)
  
  return

if __name__ == '__main__':
  main()
