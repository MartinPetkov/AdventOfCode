#!/usr/bin/env python


class CircularBuffer:
  """
  Class for a simple circular buffer.
  """

  def __init__(self, buffer, idx=0):
    self.buffer = buffer
    self.idx = idx
    self.mod = len(buffer)

  def __iter__(self):
    return self

  def __next__(self):
    val = self.buffer[self.idx]
    self.idx = (self.idx + 1) % self.mod
    return val


def part2(input):
  circ = CircularBuffer(input)

  seen = set()
  freq = 0
  for change in circ:
    if freq in seen:
      return freq

    seen.add(freq)
    freq += int(change)


def main():
  with open('input') as f:
    input = f.read().split()

  print(part2(input))


if __name__ == '__main__':
  main()
