import sys


NEIGHBORS = (
  (-1, -1),
  (-1, 0),
  (-1, 1),
  (0, -1),
  (0, 1),
  (1, -1),
  (1, 0),
  (1, 1)
)

RIGHT = (
  (-1, 0),
  (0, 1),
  (1, 0),
  (0, -1)
)

def loop(grid, start):
  visited = set()
  d = (-1, 0)
  next = 0
  while True:
    nx = (start[0] + d[0], start[1] + d[1])
    if nx not in grid.keys():
      # are we out?
      return False

    if (start, d) in visited:
      return True

    # turn right
    if grid[nx] == "#":
      next += 1
      d = RIGHT[(next) % len(RIGHT)]
      continue

    visited.add((start, d))
    start = nx


def main():
  start = tuple()
  grid = {}
  for r, line in enumerate(open(sys.argv[1]).readlines()):
    for c, col in enumerate(line.strip()):
      grid[(r, c)] = col
      if col == "^":
        start = (r, c)

  origin = start
  visited = set()
  d = (-1, 0)
  next = 0
  while True:
    nx = (start[0] + d[0], start[1] + d[1])
    if nx not in grid.keys():
      # are we out?
      break

    # turn right
    if grid[nx] == "#":
      next += 1
      d = RIGHT[(next) % len(RIGHT)]
      continue

    visited.add(nx)
    start = nx

  print(len(visited))

  canididates = set()
  for dr, dc in NEIGHBORS:
    for r, c in visited:
      if (r + dr, c + dc) in grid.keys():
        canididates.add((r + dr, c + dc))

  start = origin
  acc = 0
  for p in canididates:
    old = grid[p]
    grid[p] = "#"
    acc += loop(grid, start)
    grid[p] = old
  print(acc)


if __name__ == "__main__":
  main()
