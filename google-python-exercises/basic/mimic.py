#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Mimic pyquick exercise -- optional extra exercise.
Google's Python Class

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read
it into one giant string and split it once.

Build a "mimic" dict that maps each word that appears in the file
to a list of all the words that immediately follow that word in the file.
The list of words can be be in any order and should include
duplicates. So for example the key "and" might have the list
["then", "best", "then", "after", ...] listing
all the words which came after "and" in the text.
We'll say that the empty string is what comes before
the first word in the file.

With the mimic dict, it's fairly easy to emit random
text that mimics the original. Print a word, then look
up what words might come next and pick one at random as
the next work.
Use the empty string as the first word to prime things.
If we ever get stuck with a word that is not in the dict,
go back to the empty string to keep things moving.

Note: the standard python module 'random' includes a
random.choice(list) method which picks a random element
from a non-empty list.

For fun, feed your program to itself as input.
Could work on getting it to put in linebreaks around 70
columns, so the output looks better.

"""
import os
import random
import sys

NumArgs   = 2
NumWords  = 200
NumColumns= 70
MinWords  = 1
MaxWords  = 999
EmptyWord = ""

# Generic check functions
# Check if the value is None
def check_not_none(value):
  assert(value is not None), "Value is None"
# Check if the value is expected
def check_value(value, expected):
  assert value == expected, f"Value is {value}, but expected {expected}"
# Check if the value is greater than the expected value
def check_greater(value, expected):
  assert value > expected, f"Value is {value}, but expected greater than {expected}"
# Check if the value is lesser than the expected value
def check_lesser(value, expected):
  assert value < expected, f"Value is {value}, but expected lesser than {expected}"

def mimic_dict(filename):
  """Returns mimic dict mapping each word to list of words which follow it."""
  filehandle = open(filename, 'r')
  check_not_none(filehandle is not None)
  # read the entire file into a single string
  text = filehandle.read()
  filehandle.close()
  # split the string into a list of words
  word_list = text.split()

  # create a dictionary to hold the mimic dict
  mimic_dict = {}
  # iterate through the list of words and build the mimic dict
  for i in range(len(word_list) - 1):
    word = word_list[i]
    next_word = word_list[i + 1]
    # if the word is not in the mimic dict, add it with an empty list
    if word not in mimic_dict:
      mimic_dict[word] = []
    # append the next word to the list of words that follow the current word
    mimic_dict[word].append(next_word)
  # add the empty string as a key with the first word as its value
  mimic_dict[EmptyWord] = [word_list[0]]
  # add the empty string as next word for the last word in the list
  mimic_dict[word_list[-1]] = [EmptyWord]

  return mimic_dict


# Given mimic dict and start word, prints N random words
# the number of words to print is an optional parameter
# if not provided, defaults to 200
def print_mimic(mimic_dict, word, num_words=NumWords):
  """Given mimic dict and start word, prints 200 random words."""
  # use the empty string as default whenever the word is not in the mimic dict
  empty_string_list = mimic_dict.get(EmptyWord, [])
  check_greater(len(empty_string_list), 0)

  # maintain a column count to limit the output to 70 columns
  column_count = 0


  # print the first word unless the word is empty
  if (word != EmptyWord):
    print(word, end=' ')
    column_count += len(word) + 1

  # print num_words-1 more words
  for _ in range(num_words - 1):
    # get the list of words that follow the current word
    # if the word is not in the mimic dict, use the empty string
    # to get the first word
    next_words = mimic_dict.get(word, empty_string_list)
    
    # choose a random word from the list
    word = random.choice(next_words)
    
    # print the chosen word
    print(word, end=' ')
    column_count += len(word) + 1  

    # wrap the text to NumColumns columns
    if column_count > NumColumns:
      print()
      column_count = 0

  # print a newline at the end
  print()
  
  return  


# Provided main(), calls mimic_dict() and mimic()
def main():
  num_args = len(sys.argv)
  if num_args < NumArgs or num_args > NumArgs + 1:
    print('usage: ./mimic.py file-to-read [num-words<%i-%i>]' % (MinWords, MaxWords))
    sys.exit(1)

  num_words = NumWords
  if len(sys.argv) == NumArgs+1:
    num_words = int(sys.argv[2])
    if (num_words < MinWords or num_words > MaxWords):
      print('usage: ./mimic.py file-to-read [num-words<%i-%i>]' % (MinWords, MaxWords))
      sys.exit(1)

  file_name = sys.argv[1]
  if (os.path.isfile(file_name) == False):
    print('File does not exist: %s' % file_name)
    sys.exit(1)

  dict = mimic_dict(file_name)
  print_mimic(dict, EmptyWord, num_words)

if __name__ == '__main__':
  main()
