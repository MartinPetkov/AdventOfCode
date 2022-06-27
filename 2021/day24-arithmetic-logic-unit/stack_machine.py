# Implement part of the stack calculation from https://github.com/dphilipson/advent-of-code-2021/blob/master/src/days/day24.rs

pairs = [
  (12,9),
  (12,4),
  (12,2),
  (-9,5),
  (-9,1),
  (14,6),
  (14,11),
  (-10,15),
  (15,7),
  (-2,12),
  (11,15),
  (-15,9),
  (-9,12),
  (-3,12),
]


stack = []
i = 0
for check, offset in pairs:
  if check > 0:
    stack.append(f'input[{i}] + {offset}')
  else:
    popped_value = stack.pop(-1)
    print(f'input[{i}] == {popped_value} - {-check}')
  i += 1

print('-----')

stack = []
i = 0
for check, offset in pairs:
  if check > 0:
    stack.append(f'input[{i}] + {offset}')
  else:
    popped_value = stack.pop(-1)
    combined = int(popped_value.split()[-1]) + check
    pi = popped_value.split()[0]
    print(f'input[{i}] == {pi} {combined}')
  i += 1
