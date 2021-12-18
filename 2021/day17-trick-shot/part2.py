# Run as:
# python3 part1.py [input|sample]

import re
import sys

def draw(points, startx, endx, starty, endy):
  ay = -1
  y1 = 0
  starty, endy = sorted([starty, endy], reverse=True)
  y1 = max([starty, endy, 0] + [p[1] for p in points])

  for y in range(y1, endy+ay, ay):
    for x in range(0, endx+1):
      point = (x,y)
      if point == (0,0):
        print('S', end='')
      elif point in points:
        print('#', end='')
      elif (startx <= x <= endx) and (y in list(range(starty, endy+ay, ay))):
        print('T', end='')
      else:
        print('.', end='')
    print()


# Simply try all speed combinations upto (100,100).
def calculate_initial_speed(x_min, x_max, y_min, y_max):
  # Determine accelerations.
  # Keep them static because this works for my input and sample.
  ax = -1
  ay = -1

  highest = ((0,0), (0,0), [])
  all_v0s = set()

  # Try only up to a bounded amount of initial speed values.
  # This is still a lot of possibilities, but a manageable number.
  for v0x in range(1,1000):
    for v0y in range(-1000,1000):
      points = []
      vx, vy = v0x, v0y
      x = y = 0

      maxpoint = (x,y)

      # Increase the time continuously until we go past the bounds.
      # Speed can be 0, because we could be dropping to the bottom.
      while True:
        points.append((x,y))
        if y > maxpoint[1]:
          maxpoint = (x,y)

        # Check if we've left the bounds, in which case loop and increase the speed.
        # x only moves one way, so we can check it directly against the boundary.
        # However, y may increase, then slow down and decrease again, so
        # for it, check that the speed is negative as well.
        if x > x_max or (vy <= 0 and y < y_min):
          # Out of bounds, stop the simulation.
          break

        # Check if we've hit the boundary on both coordinates.
        if (x_min <= x <= x_max) and (y_min <= y <= y_max):
          # We hit the target area!
          # Check if this beats our highest so far.
          if maxpoint[1] > highest[1][1]:
            highest = (v0x, v0y), maxpoint, points
          # We've established we hit the area, so stop looping.
          all_v0s.add((v0x, v0y))
          break

        # Advance both x and y forward.
        x += vx
        # Stop accelerating x once it reaches 0.
        if vx != 0:
          vx += ax
        y += vy
        vy += ay

  return highest, all_v0s

def solve(data):
  targetx, targety = re.findall(r'[xy]=[\w.-]+', data)
  targetx_min, targetx_max = sorted([int(p) for p in targetx[2:].split('..')])
  targety_min, targety_max = sorted([int(p) for p in targety[2:].split('..')])
  print(f'bounds: {targetx}, {targety}')

  (v0, highest_point, points), all_v0s = calculate_initial_speed(targetx_min, targetx_max, targety_min, targety_max)
  if sys.argv[1] != 'input':
    draw(points, targetx_min, targetx_max, targety_min, targety_max)
  print(f'landed on {points[-1]} with peak {highest_point} and initial speed {v0}')
  print(f'path: {points}')
  return len(all_v0s)


def main():
  with open(sys.argv[1]) as f:
    data = f.read().strip()
  print(solve(data))

if __name__ == '__main__':
  main()
