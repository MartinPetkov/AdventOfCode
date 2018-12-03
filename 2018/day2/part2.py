#!/usr/bin/env python

import argparse


def part2(input):
  # Track all strings with each letter missing.
  # If seen, exit early.
  seen = {}
  for box_id in input:
    for i in range(len(box_id) - 1):
      if i not in seen:
        seen[i] = set()

      s = box_id[:i] + box_id[i+1:]
      if s in seen[i]:
        print(s)

      seen[i].add(s)

  

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
  
  print(part2(input))


if __name__ == '__main__':
  main()
