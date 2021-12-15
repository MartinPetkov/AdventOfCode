# Run as:
# python3 part1.py [input|sample]

import sys


def draw(graph, path):
  startx, starty = 0, 0
  endx = max(graph, key=lambda point: point[0])[0]
  endy = max(graph, key=lambda point: point[1])[1]
  for x in range(startx, endx+1):
    for y in range(starty, endy+1):
      point = (x,y)
      if point not in path:
        print(graph[point], end='')
      else:
        print('-', end='')
    print()


def solve(data):
  lines = [line.strip() for line in data.splitlines()]

  # This seems like a modified version of Dijkstra's Algorithm.
  # Approach: Explore as a BFS, but by tracking risk on each path and taking
  # the next lowest risk option.

  # Convert to a graph.
  graph = {
    (x,y): int(lines[x][y])
    for x in range(len(lines))
    for y in range(len(lines[x]))
  }

  # Track visited spots. The spot we start in is visited.
  start = (0,0)
  end = (len(lines)-1, len(lines[len(lines)-1])-1)
  visited = {}

  # Track next possible directions to expand.
  costs = {start: 0}
  options = [start]
  while options:
    cur = options.pop(0)
    x, y = cur
    neighbours = [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]
    for n in neighbours:
      # Ignore points not in the graph.
      if n not in graph:
        continue

      # Don't pursue is this is a more expensive option than one
      # we've already taken.
      if n in costs and costs[n] <= costs[cur] + graph[n]:
        continue

      # Add this as the next spot.
      costs[n] = costs[cur] + graph[n]
      options.append(n)
      visited[n] = cur

  # Now recreate the final path.
  total_risk = 0
  final_path = []
  cur = end
  while cur != start:
    final_path.insert(0, cur)
    total_risk += graph[cur]
    cur = visited[cur]
  final_path.insert(0, start)

  draw(graph, final_path)
  return total_risk


def main():
  with open(sys.argv[1]) as f:
    data = f.read().strip()
  print(solve(data))

if __name__ == '__main__':
  main()
