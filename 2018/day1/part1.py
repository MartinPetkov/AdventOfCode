#!/usr/bin/env python


def part1(input):
  return sum([int(x) for x in input])
  

def main():
  with open('input') as f:
    input = f.read().split()
  
  print(part1(input))


if __name__ == '__main__':
  main()
