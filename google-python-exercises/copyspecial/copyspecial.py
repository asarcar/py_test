#!/usr/bin/env python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil

# non-standard library imports
from utils_asarcar import check_boolean
from utils_asarcar import directory_exists, split_path, directory_exists
from utils_asarcar import file_exists, get_file_extension

# file constants
ArchiveFormat = 'zip'
OptionString1 = 'todir'
OptionArg1    = 'dir'
OptionString2 = 'tozip'
OptionArg2    = 'zipfile'
OptionPrefix  = '--'


"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them

# Get all the special files in the directories
# and store them in a list
def get_special_files(abs_dirs: str) -> list:
  special_files = []
  for abs_dir in abs_dirs:
    check_boolean(directory_exists(abs_dir), True)
    # Get the list of files in the directory
    file_names = os.listdir(abs_dir)
  
    # The special files are those that match the regex
    #   ^\S*__\S*__\S*
    # Check which files matches the pattern
    pattern = r'\S+__\S+__\S+' 
    for file_name in file_names:
      # no match means it isn't a special file
      if re.match(pattern, file_name) is None:
        continue
      abs_file_name = os.path.join(abs_dir, file_name)
      special_files.append(abs_file_name)
  
  return special_files

# Copy the special files to the directory specified by the user
# If the directory doesn't exist, create it
# If the directory exists, copy the special files to the directory
def copy_special_files(abs_file_names: list, abs_dst_dir: str) -> None:
  try:
    print(f'creating directory: {abs_dst_dir}')
    os.makedirs(abs_dst_dir, exist_ok=True)
  except OSError as e:
    print(f'error: {e}', file=sys.stderr)
    return
  
  # Copy the special files to the directory
  for abs_file_name in abs_file_names:
    _, base_file_name = split_path(abs_file_name)
    new_abs_file_name = os.path.join(abs_dst_dir, base_file_name)
    # Copy the file to the directory
    try:
      shutil.copy(abs_file_name, abs_dst_dir)
    except OSError as e:
      print(f'error: {e}', file=sys.stderr)
      continue

  return

#
# Zip the special files to the directory specified by the user
# We've not used the 'zip -j' command directly from the commands package
# using commands.getstatusoutput(cmd) - this package is deprecated
# and not recommended. Instead we are using the shutil.make_archive
# however the zip file is created by putting all files in a directory
# this may ignore files from different directories that are copied to the 
# same directory.
# Will fix it later by using subprocess.run(cmd, shell=True)
# command = ["zip", "-j", zip_file, file1, file2, ]
#
def zip_special_files(abs_file_names: list, abs_dst_dir: str, abs_zip_file: str) -> None:
  check_boolean(directory_exists(abs_dst_dir), True)

  # Check if the zip file already exists
  # Otherise create the zip archive
  try:
    # Remove the file if it exists
    full_abs_zip_file = abs_zip_file + '.' + ArchiveFormat
    if file_exists(full_abs_zip_file):
      print(f"Will overwrite existing zip file: {full_abs_zip_file}")
    
    # Create the zip archive
    shutil.make_archive(abs_zip_file, ArchiveFormat, abs_dst_dir)
    print(f"Successfully created {abs_zip_file} from {abs_dst_dir}")

  except Exception as e:
    print(f"An error occurred: {e}", file=sys.stderr)  
  
  return

# Extract all the special files from the directories
# and store them in a list
def get_abs_dirs(args: list) -> list:
  abs_dirs = []
  for arg in args:
    # Validate all the remaining args are directories AND
    # Ensure the directories are not the same as todir AND
    # Check that the directory exists
    if not directory_exists(arg):
      print(f'error: ignoring {arg} as not a dir', file=sys.stderr)
      continue

    # ensure directory is not the same as todir
    abs_dir = os.path.abspath(arg)
    if (abs_dir in abs_dirs):
      print(f'error: ignoring {arg} as same as previous dir', 
            file=sys.stderr)
      continue
    
    # add this directory to the list of directories
    abs_dirs.append(abs_dir)
  return abs_dirs

def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  arg_str1 = OptionPrefix + OptionString1
  arg_str2 = OptionPrefix + OptionString2

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print(f"usage: [{arg_str1} {OptionArg1}] [{arg_str2} {OptionArg2}] dir [dir ...]", 
          file=sys.stderr);
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if len(args) > 0 and args[0] == arg_str1:
    if len(args) < 2 or not args[1] or args[1].startswith(OptionPrefix):
      print(f"error: {arg_str1} requires a {OptionArg1} argument", file=sys.stderr)
      sys.exit(1)
    todir = args[1]
    del args[0:2]

  tozip = ''
  if len(args) > 0 and args[0] == arg_str2:
    if (len(args) < 2 or not args[1] or 
        args[1].startswith(OptionPrefix)):
      print(f"error: {arg_str2} requires a {OptionArg2} argument", 
            file=sys.stderr)
      sys.exit(1)
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print(f'error: must specify one or more dirs', file=sys.stderr)
    sys.exit(1)

  # +++your code here+++
  # accumulate all the dirs form where we are extracting special files
  abs_dirs = get_abs_dirs(args)

  # accumulate the special files in a list
  # Get the special files from the directories
  abs_file_names = get_special_files(abs_dirs)

  # if todir is NOT set, abspath just gets set to current directory  
  # in either case just PRINT the special files and we are done
  # nothing to copy in a special directory or zip the todir

  # Get the absolute path of the directory.
  abs_dst_dir = os.path.abspath(todir)
  abs_cur_dir = os.path.abspath(os.getcwd())

  if abs_dst_dir == abs_cur_dir:
    print(f"Printing all special files and exiting as copy directory not set")
    print(f"# of special files: {len(abs_file_names)}")
    i = 0
    for abs_file_name in abs_file_names:
      i += 1
      print(f"#{i}: {abs_file_name}")
    return
  
  # Copy the special files to the todir directory
  copy_special_files(abs_file_names, abs_dst_dir)

  # if tozip is not set, we are done
  if not tozip:
    return

  # zip the special files -  get the absolute path of the zipfile. 
  # By default absolute path assumes the current working directory
  abs_zip_file = os.path.abspath(tozip)
  zip_special_files(abs_file_names, abs_dst_dir, abs_zip_file)

  return

if __name__ == "__main__":
  main()
