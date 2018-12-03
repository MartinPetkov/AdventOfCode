#!/usr/bin/env python

import argparse


def check_letters(s, num_letters):
  for l in set(s):
    if s.count(l) == num_letters:
      return True

  return False


def part1(input):
  two_letters = 0
  three_letters = 0
  for box_id in input:
    if check_letters(box_id, 2):
      two_letters += 1

    if check_letters(box_id, 3):
      three_letters += 1

  return two_letters * three_letters
  

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument(
    '-f',
    default='input.txt',
    dest='input_file',
  )

  args = parser.parse_known_args()[0]
  
  input_file = args.input_file

  with open(input_file) as f:
    input = f.readlines()
  
  print(part1(input))


if __name__ == '__main__':
  main()
