# Run as:
# python3 part1.py [input|sample]

import math
import sys


class Snail:
  def __init__(self, left=None, right=None, val=None, parent=None):
    self.parent = parent
    self.leaf = False
    if val is not None:
      self.val = val
      self.leaf = True
      self.left = None
      self.right = None
    else:
      self.left = left
      self.right = right
      self.left.parent = self
      self.right.parent = self

  def _repr_with_depth(self, depth=0):
    prefix = (' ' * (len('Snail[_]') + 1)) * depth
    if self.leaf:
      return prefix + f'{self.val}'

    s = ''
    s += f'{self.right._repr_with_depth(depth+1)}\n'
    s += prefix + f'Snail[{depth}]\n'
    s += f'{self.left._repr_with_depth(depth+1)}\n'
    return s

  def _repr_brackets(self):
    if self.leaf:
      return f'{self.val}'
    return f'[{self.left._repr_brackets()},{self.right._repr_brackets()}]'

  def __repr__(self):
    #return self._repr_with_depth()
    return self._repr_brackets()

  def __add__(self, other):
    snail = Snail(self, other)

    # Reduce the resulting snail
    work_remaining = True
    while work_remaining:
      # Assume there's nothing more to do.
      # This assumption can be falsified later.
      work_remaining = False

      # Look for exploding nodes.
      bomb = find_bomb(snail)
      if bomb:
        work_remaining = True
        explode(bomb)
        continue

      # Look for splitting nodes.
      splitter = find_splitter(snail)
      if splitter:
        work_remaining = True
        split(splitter)
        continue

    return snail

  def magnitude(self):
    if self.leaf:
      return self.val
    return (3 * self.left.magnitude()) + (2 * self.right.magnitude())


# Look for an exploding pair rooted at this tree.
# If any pair is nested inside four pairs, the leftmost such pair explodes.
def find_bomb(snail, depth=0):
  if depth >= 4 and not snail.leaf:
    return snail

  if snail.leaf:
    return None

  # Go left first, then right.
  return find_bomb(snail.left, depth+1) or find_bomb(snail.right, depth+1) or None


# Helper: Find the leftmost value and add the bomb value to it.
# Need to branch left at least once, then branch right before left, and look
# for a leaf.
def add_to_left(cur, bomb_val, branched_left=False):
  # We've finally found a leaf.
  if cur.leaf:
    cur.val += bomb_val
    return True

  # If we've already branched left, then just do a normal right-left recursion.
  if branched_left:
    return add_to_left(cur.right, bomb_val, True) or add_to_left(cur.left, bomb_val, True)

  # We can't go anymore up, stop.
  if not cur.parent:
    return False

  # Else, try the parent.
  # If we are the left branch, continue up.
  if cur == cur.parent.left:
    return add_to_left(cur.parent, bomb_val, False)

  # Otherwise, we're the right branch.
  # So take the parent's left branch and note that we've branched.
  return add_to_left(cur.parent.left, bomb_val, True)

# Helper: Find the rightmost value and add the bomb value to it.
# Need to branch right at least once, then branch left before right, and look
# for a leaf.
def add_to_right(cur, bomb_val, branched_right=False):
  # We've finally found a leaf.
  if cur.leaf:
    cur.val += bomb_val
    return True

  # If we've already branched right, then just do a normal left-right recursion.
  if branched_right:
    return add_to_right(cur.left, bomb_val, True) or add_to_right(cur.right, bomb_val, True)

  # We can't go anymore up, stop.
  if not cur.parent:
    return False

  # Else, try the parent.
  # If we are the right branch, continue up.
  if cur == cur.parent.right:
    return add_to_right(cur.parent, bomb_val, False)

  # Otherwise, we're the left branch.
  # So take the parent's right branch and note that we've branched.
  return add_to_right(cur.parent.right, bomb_val, True)

# To explode a pair, the pair's left value is added to the first regular number
# to the left of the exploding pair (if any), and the pair's right value is
# added to the first regular number to the right of the exploding pair (if any).
# Exploding pairs will always consist of two regular numbers. Then, the entire
# exploding pair is replaced with the regular number 0.
def explode(bomb):
  # Add the numbers to the right and left respectively.
  add_to_left(bomb, bomb.left.val)
  add_to_right(bomb, bomb.right.val)

  # Replace the node with a 0.
  bomb.left = None
  bomb.right = None
  bomb.leaf = True
  bomb.val = 0

# Look for a splitting number.
# If any regular number is 10 or greater, the leftmost such regular number
# splits.
def find_splitter(snail):
  if snail.leaf:
    if snail.val >= 10:
      return snail
    return None

  # Go left first, then right.
  return find_splitter(snail.left) or find_splitter(snail.right) or None

# To split a regular number, replace it with a pair; the left element of the
# pair should be the regular number divided by two and rounded down, while the
# right element of the pair should be the regular number divided by two and
# rounded up.
def split(splitter):
  splitter.left = Snail(val=math.floor(splitter.val / 2), parent=splitter)
  splitter.right = Snail(val=math.ceil(splitter.val / 2), parent=splitter)
  splitter.val = None
  splitter.leaf = False


def list_to_snail(lst):
  # Assumes input is a valid snail number represented as a list.
  left, right = lst[0], lst[1]

  left = list_to_snail(left) if isinstance(left, list) else Snail(val=left)
  right = list_to_snail(right) if isinstance(right, list) else Snail(val=right)

  return Snail(left, right)


def solve(data):
  lines = [line.strip() for line in data.splitlines()]

  # Try out all permutations.
  maxnitude = 0
  for i in range(len(lines)):
    for j in range(len(lines)):
      if j == i:
        continue
      snail1 = list_to_snail(eval(lines[i]))
      snail2 = list_to_snail(eval(lines[j]))
      snail = snail1 + snail2
      magnitude = snail.magnitude()
      if magnitude > maxnitude:
        maxnitude = magnitude

  return maxnitude


def main():
  with open(sys.argv[1]) as f:
    data = f.read().strip()
  print(solve(data))

if __name__ == '__main__':
  main()
