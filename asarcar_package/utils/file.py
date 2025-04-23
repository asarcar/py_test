#!/usr/bin/python3

# Copyright 2025 Arijit Sarcar.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

import os

def file_exists(filename):
  return os.path.exists(filename)

def get_file_extension(filename):
  return os.path.splitext(filename)[1]
