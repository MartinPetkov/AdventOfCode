#!/usr/bin/env python

import argparse


def part1(input):
  # TODO: Implement
  pass
  

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
    input = [l.strip() for l in f.readlines()]
  
  print(part1(input))


if __name__ == '__main__':
  main()
