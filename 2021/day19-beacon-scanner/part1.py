# Run as:
# python3 part1.py [input|sample]

# I couldn't really figure this one out :(

import math
import sys


class Point:
  def __init__(self, coord):
    self.x = coord[0] if len(coord) > 0 else 0
    self.y = coord[1] if len(coord) > 1 else 0
    self.z = coord[2] if len(coord) > 2 else 0


def to_point(str_point):
  return tuple(int(c) for c in str_point.split(','))

def magnitude(p1, p2):
  sqrsum = sum([(p2[i]-p1[i])**2 for i in range(len(p1))])
  return format(math.sqrt(sqrsum), '.4f')

def points_to_magnitudes(points):
  magnitudes = {}
  for i in range(0, len(points)-1):
    for j in range(i+1, len(points)):
      point1 = to_point(points[i])
      point2 = to_point(points[j])

      mag = magnitude(point1, point2)
      if mag not in magnitudes:
        magnitudes[mag] = set()

      magnitudes[mag].add(point1)
      magnitudes[mag].add(point2)

  return magnitudes

def points_in_common(scanner1, scanner2):
  # Look for matching magnitudes and count points seen by both scanners.
  scanner1_points = set()
  scanner2_points = set()
  for mag in scanner1:
    if mag in scanner2:
      scanner1_points |= scanner1[mag]
      scanner2_points |= scanner2[mag]

  return max(len(scanner1_points), len(scanner2_points))

def all_points(scanner1, scanner2):
  # First find all points that scanner1 sees, and remember which ones overlap with scanner2.
  points1 = set()
  overlap_points2 = set()
  for mag in scanner1:
    points1 |= scanner1[mag]
    if mag in scanner2:
      overlap_points2 |= scanner2[mag]

  # Now look at all points in scanner2 which don't overlap.
  points2 = set()
  for mag in scanner2:
    for point in scanner2[mag]:
      if point not in overlap_points2:
        points2.add(point)

  return len(points1) + len(points2)


def solve(data):
  # Represent scanners as a map of magnitudes to sets of points
  # This uses the magnitude function:
  # M((x1,y1),(x2,y2)) = sqrt((x2-x1)^2 + (y2-y1)^2)
  scanners = []

  points = []
  for line in data.splitlines()[1:]:
    if not line.strip():
      continue

    if 'scanner' in line:
      # Calculate magnitudes and start new set of points
      scanner = points_to_magnitudes(points)
      scanners.append(scanner)
      points = []
      continue

    # Otherwise it's a point.
    points.append(line.strip())
  scanner = points_to_magnitudes(points)
  scanners.append(scanner)

  # Look for points in common
  total_points = 0
  for i in range(0, len(scanners)-1):
    for j in range(i+1, len(scanners)):
      common = points_in_common(scanners[i], scanners[j])
      allp = all_points(scanners[i], scanners[j])
      total_points += allp
      print(f'Scanner {i} and Scanner {j} have {allp} points between them')
  print(f'{total_points} total beacons')

  return None


def main():
  with open(sys.argv[1]) as f:
    data = f.read().strip()
  print(solve(data))

if __name__ == '__main__':
  main()
