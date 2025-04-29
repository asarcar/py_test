#!/usr/bin/env python3

# Copyright 2025 Arijit Sarcar.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

import os

def directory_exists(directory: str) -> bool:
  if not os.path.exists(directory):
    return False
  return os.path.isdir(directory)

def split_path(path: str) -> tuple:
  """
  Splits the path into directory and file name
  :param path: The path to split
  :return: A tuple containing the directory and file name
  """
  norm_path = os.path.normpath(path)
  if (not os.path.exists(norm_path)):
    raise ValueError(f"Path '{norm_path}' is not a valid path")
  directory, filename = os.path.split(path)
  return directory, filename

def file_exists(filename: str) -> bool:
  if not os.path.exists(filename):
    return False
  return os.path.isfile(filename)

def get_file_extension(filename: str) -> str:
  return os.path.splitext(filename)[1]
