# Run as:
# python3 part1.py [input|sample]

import sys

class Node:
  def __init__(self, val, friends=None):
    self.val = val
    self.friends = friends or set()

  def big_guy_4u(self):
    return self.val.isupper()

# Explore out from this path.
# The explorer is standing on the last spot in the path.
def explore(graph, path):
  # Find all the places we can visit.
  current = path[-1]

  # If we've reached the end, announce it and stop exploring.
  if current.val == 'end':
    print(','.join([p.val for p in path]))
    return 1

  return sum([
    explore(graph, path + [friend])
    for friend in current.friends
    # Only continue through big caves and unseen spots.
    if friend.big_guy_4u() or friend not in path
  ])


def solve(data):
  lines = [line.strip() for line in data.splitlines() if line.strip()]

  # Parse the lines into a graph.
  graph = {}
  for line in lines:
    # Retrieve or create the new nodes
    val1, val2 = line.split('-')
    if val1 not in graph:
      graph[val1] = Node(val1)
    if val2 not in graph:
      graph[val2] = Node(val2)
    node1 = graph[val1]
    node2 = graph[val2]

    # Add the connections.
    node1.friends.add(node2)
    node2.friends.add(node1)

  return explore(graph, [graph['start']])


def main():
  with open(sys.argv[1]) as f:
    data = f.read().strip()
  print(solve(data))

if __name__ == '__main__':
  main()
