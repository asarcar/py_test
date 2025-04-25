#!/usr/bin/env python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python 
# Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

# non-standard library imports
from utils_asarcar import file_exists

# +++your code here+++
SummaryString = 'summary'
SummaryFileArgs = '--'+ SummaryString + 'file'

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(file_name):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++
  fp = open(file_name, 'r')
  text = fp.read()
  fp.close()

  # Extract the strings 'year', 'name rank', ... list
  # extract year from '<h3 align="center">Popularity in 1990</h3>'
  pattern = r'<h\d.*>Popularity in (\d+)</h\d>'
  year = re.search(pattern, text)
  if not year:
    sys.stderr('No year found in file: %s' % file_name)
    sys.exit(1)  
  name_list = [year.group(1)]

  # re.findall returns a list of tuples - unwind those tuples and add to dictionary 
  name_rank = {}
  # extract name and rank #s from '<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>'
  pattern = r'<tr align="right"><td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>'
  # arrange the dictionary alphanumerically
  for (rank, male_name, female_name) in re.findall(pattern, text):
    # if the name already exists, keep the lowest rank
    # if the name does not exist, add it to the dictionary
    name_rank[male_name] = name_rank.get(male_name, rank)
    name_rank[female_name] = name_rank.get(female_name, rank)
  
  # sort the dictionary by key
  name_sorted = sorted(name_rank.keys())

  # return the sorted list of names
  for name in name_sorted:
    name_list.append(name + " " + name_rank[name])
  
  return name_list

def write_names(file_name, name_list):
  fp = open(file_name, 'w')
  fp.write('\n'.join(name_list))
  fp.close()
  return

def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself. no args => argv[1:] is defined as empty list
  args = sys.argv[1:]

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if not args or args[0] == SummaryFileArgs and len(args) == 1:
    # If no args, or only the summary flag, print usage and exit.
    print('usage: [%s] file [file ...]'% SummaryFileArgs)
    sys.exit(1)

  if args[0] == SummaryFileArgs:
    summary = True
    del args[0]
  
  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  for file_name in args:
    if not file_exists(file_name):
      print('File does not exist: %s' % file_name)
      sys.exit(1)

    # Extract the year and names from the file
    name_list = extract_names(file_name)
    
    # If the summary flag is not set, write the names to a summary file
    if not summary: 
      print('\n'.join(name_list))
      continue
    
    # Write the names to file_name.summary
    write_names(file_name + "." + SummaryString, name_list)  
  
  return

if __name__ == '__main__':
  main()
