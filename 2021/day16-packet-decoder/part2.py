# Run as:
# python3 part1.py [input|sample]

import operator
import sys

from itertools import islice
from functools import reduce


class Packet:
  TYPES = {
    4: 'LITERAL_VALUE',
    0: 'OPERATOR_SUM',
    1: 'OPERATOR_PRODUCT',
    2: 'OPERATOR_MIN',
    3: 'OPERATOR_MAX',
    5: 'OPERATOR_GREATER_THAN',
    6: 'OPERATOR_LESS_THAN',
    7: 'OPERATOR_EQUAL',
  }

  '''Class representing a parsed packet.'''
  def __init__(self, version, type_id, type_name, value=None, subpackets=None):
    self.version = version
    self.type_id = type_id
    self.type_name = type_name
    self.value = value
    self.subpackets = subpackets or []

  def __repr__(self):
    return f'<Packet v{self.version}; type={self.type_name}; value={self.value}; subpackets={self.subpackets}>'

  def version_sum(self):
    vsum = self.version
    if isinstance(self.value, list):
      vsum += sum([p.version_sum() for p in self.value])
    return vsum


'''Helper functions for bit manipulation.'''
# Convert a hex string to its bit form.
def hexbits(h):
  # Need to consider 0s in the beginning of the hex string.
  # Pad each hexchar to the number of bits required to represent a hex char.
  s = ''.join([f'{int(hexchar,16):0{4}b}' for hexchar in h])
  # Pad with 0s at the front until it's a multiple of 4.
  padding = (4 - (len(s) & 3)) & 3
  return ('0' * padding) + s

# Convert a string to a generator.
def to_gen(s):
  return (c for c in s)

# Consumes some bits from a generator.
# If None, consumes the rest of it.
def consume(gen, n=None):
  return ''.join(islice(gen, n))


'''Functions for parsing bits as different values.'''
# Bit parser for literal values.
def parse_literal(bits):
  literal = ''
  # Consume 5 bits until the end of the groups.
  while True:
    group = consume(bits, 5)
    # If we're out of groups, exit.
    if not group:
      break

    literal += group[1:]

    # If it starts with a 0, this was the last group.
    if group[0] == '0':
      break

  return int(literal, 2)

# Bit parser for a packet operator.
# Treats the remaining bits as sub-packets to parse.
def parse_operator(bits):
  # The first bit is the length type id
  length_type_id = consume(bits, 1)

  # If the length type ID is 0, then the next 15 bits are a number that represents the total length in bits of the sub-packets contained by this packet.
  subpackets = []
  if length_type_id == '0':
    subpackets_length_bits = int(consume(bits, 15), 2)
    subpackets_bits = to_gen(consume(bits, subpackets_length_bits))
    # Now repeatedly parse the remaining bits until we run out.
    while True:
      subpacket = parse_packet(subpackets_bits)
      if not subpacket:
        break
      subpackets.append(subpacket)

  # If the length type ID is 1, then the next 11 bits are a number that represents the number of sub-packets immediately contained by this packet
  else:
    subpackets_num = int(consume(bits, 11), 2)
    # Consume an exact number of packets.
    for _ in range(subpackets_num):
      subpackets.append(parse_packet(bits))

  return subpackets

def calculate_value(packet):
  # Calculate the value based on the packet's type.
  # 4: 'LITERAL_VALUE',
  if packet.type_id == 4:
    return packet.value

  # 0: 'OPERATOR_SUM',
  elif packet.type_id == 0:
    return reduce(operator.add, [p.value for p in packet.subpackets], 0)

  # 1: 'OPERATOR_PRODUCT',
  elif packet.type_id == 1:
    return reduce(operator.mul, [p.value for p in packet.subpackets], 1)

  # 2: 'OPERATOR_MIN',
  elif packet.type_id == 2:
    return reduce(min, [p.value for p in packet.subpackets])

  # 3: 'OPERATOR_MAX',
  elif packet.type_id == 3:
    return reduce(max, [p.value for p in packet.subpackets])

  # 5: 'OPERATOR_GREATER_THAN',
  elif packet.type_id == 5:
    return 1 if packet.subpackets[0].value > packet.subpackets[1].value else 0

  # 6: 'OPERATOR_LESS_THAN',
  elif packet.type_id == 6:
    return 1 if packet.subpackets[0].value < packet.subpackets[1].value else 0

  # 7: 'OPERATOR_EQUAL',
  elif packet.type_id == 7:
    return 1 if packet.subpackets[0].value == packet.subpackets[1].value else 0

# This function may recursively call itself to parse sub-packets.
# Expects a generator returning bits. The recursive calls take the
# remaining bits, so only one pass is performed through all the bits.
def parse_packet(bits):
  # There may not be any more bits to consume.
  version_bits = consume(bits, 3)
  if version_bits == '':
    return None

  # Otherwise, assume we have enough bits left to build a correct packet.

  # The first 3 bits are the version.
  version = int(version_bits, 2)

  # The next 3 bits are the type ID.
  type_id = int(consume(bits, 3), 2)
  type_name = Packet.TYPES[type_id]
  packet = Packet(version, type_id, type_name)

  # Parse the value based on the type id, if recognized and parseable.
  if type_id == 4:
    # Literal value, just set the value.
    packet.value = parse_literal(bits)
  else:
    # It's an operator.
    # Get the subpackets first, then reduce.
    packet.subpackets = parse_operator(bits)
    packet.value = calculate_value(packet)

  return packet


def solve(data):
  lines = [line.strip() for line in data.splitlines()]

  for line in lines:
    # Step 1: Convert to bits and remove trailing 0s
    # Convert to generator so we can "consume" bits from it.
    bits = to_gen(hexbits(line))

    # This is the outermost packet.
    packet = parse_packet(bits)
    print(f'{line} = {packet.value} {packet}')

  return packet.value


def main():
  with open(sys.argv[1]) as f:
    data = f.read().strip()
  print(solve(data))

if __name__ == '__main__':
  main()
