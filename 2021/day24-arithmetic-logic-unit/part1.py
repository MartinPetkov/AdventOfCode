# Run as:
# python3 part1.py [input|sample]

import sys


class ALU:
  def __init__(self):
    self.reg = {
      'w': 0,
      'x': 0,
      'y': 0,
      'z': 0,
    }

  def __repr__(self):
    return f'w={self.reg["w"]} ; x={self.reg["x"]} ; y={self.reg["y"]} ; z={self.reg["z"]}'

  def load_value(self, reg_or_value):
    return int(self.reg.get(reg_or_value, reg_or_value))

  def inp(self, a):
    '''Read an input value and write it to variable a.'''
    self.reg[a] = int(input())

  def add(self, a, b):
    '''Add the value of a to the value of b, then store the result in variable a.'''
    self.reg[a] = self.load_value(a) + self.load_value(b)

  def mul(self, a, b):
    '''Multiply the value of a by the value of b, then store the result in variable a.'''
    self.reg[a] = self.load_value(a) * self.load_value(b)

  def div(self, a, b):
    '''Divide the value of a by the value of b, truncate the result to an integer, then store the result in variable a. (Here, "truncate" means to round the value toward zero.)'''
    a_val = self.load_value(a)
    b_val = self.load_value(b)
    if b_val == 0:
      raise Exception('cannot div with b=0')
    self.reg[a] = int(a_val / b_val)

  def mod(self, a, b):
    '''Divide the value of a by the value of b, then store the remainder in variable a. (This is also called the modulo operation.)'''
    a_val = self.load_value(a)
    b_val = self.load_value(b)
    if a_val < 0 or b_val <= 0:
      raise Exception('cannot mod with a<0 or b<=0')
    self.reg[a] = a_val % b_val

  def eql(self, a, b):
    '''If the value of a and b are equal, then store the value 1 in variable a. Otherwise, store the value 0 in variable a.'''
    self.reg[a] = int(self.load_value(a) == self.load_value(b))


def solve(data):
  lines = [line.strip() for line in data.splitlines() if line.strip()]

  alu = ALU()
  for instruction in lines:
    print(instruction)
    op, args = instruction.split(' ', 1)
    args = args.split(' ')
    getattr(alu, op)(*args)
    if instruction == 'add z y':
      print(f'{alu}\n')

  return alu

def main():
  with open(sys.argv[1]) as f:
    data = f.read().strip()
  print(solve(data))

if __name__ == '__main__':
  main()
