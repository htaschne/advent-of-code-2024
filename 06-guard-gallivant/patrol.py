import sys


def loop(grid, start):
  visited = set()
  d = (-1, 0)
  while True:
    nx = (start[0] + d[0], start[1] + d[1])
    if nx not in grid.keys():
      # are we out?
      return False

    if (start, d) in visited:
      return True

    # turn right
    if grid[nx] == "#":
      if d == (-1, 0):
        d = (0, 1)
      elif d == (0, 1):
        d = (1, 0)
      elif d == (1, 0):
        d = (0, -1)
      else:
        d = (-1, 0)
      continue

    visited.add((start, d))
    start = nx


def main():
  start = tuple()
  mr, mc = 0, 0
  grid = {}
  for r, line in enumerate(open(sys.argv[1]).readlines()):
    for c, col in enumerate(line.strip()):
      grid[(r, c)] = col
      if col == "^":
        start = (r, c)
      mr = max(r, mr)
      mc = max(c, mc)

  origin = start
  visited = set()
  d = (-1, 0)
  while True:
    nx = (start[0] + d[0], start[1] + d[1])
    if nx not in grid.keys():
      # are we out?
      break

    # turn right
    if grid[nx] == "#":
      if d == (-1, 0):
        d = (0, 1)
      elif d == (0, 1):
        d = (1, 0)
      elif d == (1, 0):
        d = (0, -1)
      else:
        d = (-1, 0)

      continue

    visited.add(nx)
    start = nx

  print(len(visited))

  canididates = set()
  for dr, dc in [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
  ]:
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
