#!/usr/bin/env python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
from   urllib import request

# non-standard library imports
from   flask import Flask, render_template, send_file

# non-standard library imports
from   utils_asarcar import check_boolean
from   utils_asarcar import directory_exists, file_exists, link_exists 
from   utils_asarcar import split_path, get_file_extension

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""
TemplatesDir  = 'templates'
StaticDir     = 'static'
LocalHost     = "0.0.0.0"
IndexFileName = 'index.html'
PrefixHost    = 'http://'

def read_urls(filename: str) -> list:
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Puzzle URL: 10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  # +++your code here+++
  if not file_exists(filename):
    print(f'File {filename} does not exist', file=sys.stderr)
    return []
  
  # Extract the hostname from the filename
  # filename is in the form of <attribute>_<hostname>
  # split the filename into <attribute> and <hostname>
  # and use the hostname to create the full URL
  hostname = filename.split('_')[1]
  
  # read the entire apache log into log
  fh = open(filename, 'r')
  log = fh.read()
  fh.close()
  
  # find all instances where urls have the puzzle pattern as specified below
  url_dict = {}
  pattern = r'GET (\S+/puzzle/\S+\.jpg) HTTP/1.0'
  urls = re.findall(pattern, log)

  # eliminate duplicates by adding all of them in a dictionary
  for url in urls:
    full_url = PrefixHost + hostname + url
    url_dict[full_url] = True

  # sort all URL entries stored in the dictionary and return them in a list
  # we sort by retrieving all the keys and return the sorted list
  # use custom sort order based on the last part of the URL
  def sort_key(full_url):
    """Returns the last part of the URL to be used for sorting
    if the URL is in the form of /~foo/puzzle-bar-aaab.jpg
    otherwise returns the URL itself
    """
    sort_pattern = r'\S*-\S+-(\S+)\.jpg'
    m = re.match(sort_pattern, full_url)
    if m:
      return m.group(1)
    return full_url
  
  
  return sorted(url_dict.keys(), key=sort_key)

def download_images(img_urls: list, dest_dir: str)  -> list:
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  # Create directory if it does not exist
  abs_dst_dir = os.path.abspath(dest_dir)
  if not directory_exists(abs_dst_dir):
    print(f'Creating directory: {abs_dst_dir} as it does not exist')

  try:
    os.makedirs(abs_dst_dir, exist_ok=True)
  except OSError as e:
    print(f'error: {e}', file=sys.stderr)
    return
    
  # url is the image url and filename is the local file name
  # The local file name is the destination directory + '/' + img0, img1, etc.
  i = 0
  img_names = []
  for img_url in img_urls:
    # Download URL should be fully qualified
    img_name = f'img{i}'
    i += 1
    img_names.append(img_name)
    abs_img_file = os.path.join(abs_dst_dir, img_name)
    print(f'Retrieving image {img_url} and saving it to {abs_img_file}')
    request.urlretrieve(img_url, abs_img_file)

  return img_names

def create_html(img_names: list) -> None:
  """Creates an index.html file in the given directory
  with an img tag to show each local image file.
  """
 
  # create the content for index.html
  # <html><body>
  # <h1>Welcome to the Logpuzzle</h1>
  # <img src="{{ url_for('static', filename='img0') }}" alt="Image 1">
  # </body></html>
  i = 0
  html_text = '<html>\n<body>\n'
  html_text += '<h1>Welcome to the Logpuzzle</h1>\n'
  for img_name in img_names:
    html_text += f'<img src=\"{{{{ url_for(\'static\', filename=\'{img_name}\') }}}}" alt=\"Image {i}\">\n'
    i += 1
  html_text += '</body>\n</html>\n'

  return html_text  

def create_index(img_names: list, todir: str)  -> None:
  """"Given the image names create an index.html file
  that references the images """
  
  html_text = create_html(img_names)

  # write the index.html file in default current directory
  index_filename = os.path.join(todir, IndexFileName)
  fh = open(index_filename, 'w')
  fh.write(html_text)
  fh.close()

  return

def setup_run_web_svr(todir: str) -> None:
  if directory_exists(TemplatesDir) and link_exists(TemplatesDir):
    print(f'Deleting: {TemplatesDir} link as it already exists', file=sys.stderr)
    os.unlink(TemplatesDir)
  if directory_exists(StaticDir) and link_exists(StaticDir):
    print(f'Deleting: {StaticDir} link as it already exists', file=sys.stderr)
    os.unlink(StaticDir)
  
  os.symlink(todir, TemplatesDir)
  os.symlink(todir, StaticDir)
  
  app.run(host=LocalHost, port=50100, debug=True)


def main():
  args = sys.argv[1:]

  if not args:
    print('usage: [--todir dir] logfile')
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])

  if not todir:
    print('\n'.join(img_urls))
    return    

  # download the images, create index.html and create a symbolic link
  # to the templates directory and static directory  
  img_names = download_images(img_urls, todir)
  create_index(img_names, todir)
  setup_run_web_svr(todir)

  return

app = Flask(__name__,
            template_folder=os.path.abspath(TemplatesDir),
            static_folder=os.path.abspath(StaticDir))

# Root URL
@app.route("/")
def render_base():
    return render_template(IndexFileName)

# Test: curl localhost:50100/images/<img-name> --output <img-copy-name>
# or wget localhost:50100/images/<img-name>
# URL for each image
@app.route('/images/<filename>')
def get_image(filename):
  return send_file(os.path.join(StaticDir, filename))

if __name__ == '__main__':
  main()