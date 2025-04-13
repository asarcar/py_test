#!/usr/bin/python3

# Copyright 2025 Arijit Sarcar.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

import array
from enum import Enum
import os
import sys

# modulo 3
class Number(Enum):
  ONE     = 0
  TWO     = 1
  THREE   = 2
  
  def __str__(self):
    return self.name

class Color(Enum):
  RED     = 0
  GREEN   = 1
  PURPLE  = 2 

  def __str__(self):
    return self.name

class Shape(Enum):
  DIAMOND = 0 
  OVAL    = 1
  SQUIGLE = 2 

  def __str__(self):
    return self.name

class Shade(Enum):
  SOLID   = 0
  HOLLOW  = 1
  SHADE   = 2

  def __str__(self):
    return self.name

class Pos(Enum):
  NUMBER  = 0
  COLOR   = 1
  SHAPE   = 2
  SHADE   = 3

NumAttrs  = 4
NumSet    = 3
NumCards  = 12

class Card:
  def __init__(self, attr_list):      
    self.attributes =(  Number[attr_list[Pos.NUMBER.value]], 
                        Color[attr_list[Pos.COLOR.value]], 
                        Shape[attr_list[Pos.SHAPE.value]], 
                        Shade[attr_list[Pos.SHADE.value]] )

  def __str__(self):
    str = self.attributes[0].name
    for i in range(1, NumAttrs):
      str = str + "\t%s"%self.attributes[i]
    return str

  def get_attribute_value(self, pos):
    return self.attributes[pos].value

def check_value(value, expected):
  assert value == expected, f"Value is {value}, but expected {expected}"  

def is_set(cards):
  check_value(len(cards), NumSet)
  
  # maintain a modulo 3 running count against each attribute
  parity = []
  for i in range(NumAttrs):
    parity.append(0)

  for card in cards:
    for i in range(NumAttrs):
      parity[i] = (parity[i] + card.get_attribute_value(i)) % NumSet
  
  for i in range(NumAttrs):
    if parity[i] != 0: 
      return False

  return True


def print_cards(cards):
  print("Card #\tNumber\tColor\tShape\tShade")
  print("------\t------\t-----\t-----\t-----")
  i=0
  for card in cards:
    print("%i\t%s" %(i, card))
    i=i+1
  return

def read_cards(filename):
  """Creates an array of cards from game set reading from filename."""
  assert(os.path.isfile(filename))
  filehandle = open(filename, 'r')
  cards = []

  for line in filehandle:
    if (line[0] == '#'): continue
    attr_list = line.split()
    check_value(len(attr_list), NumAttrs+1)
    cards.append(Card(attr_list[1:]))
  filehandle.close()

  return(cards)

def print_sets(cards):
  num_sets  = 0
  num_cards = len(cards)
  for first in range(num_cards-2):
    for second in range(first+1, num_cards-1):
      for third in range(second+1, num_cards):
        if (not is_set([cards[first], cards[second], cards[third]])): continue
        # we've found a set!
        num_sets = num_sets + 1
        print("(set# %i [%i %s]\t[%i %s]\t[%i %s]" 
              %(num_sets, first, cards[first], second, cards[second], third, cards[third]))
        
  return

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
  if len(sys.argv) != 2:
    print('usage: ./set.py filename')
    sys.exit(1)

  filename = sys.argv[1]
  cards = read_cards(filename)
  print_cards(cards)
  print_sets(cards)
  return

if __name__ == '__main__':
  main()
