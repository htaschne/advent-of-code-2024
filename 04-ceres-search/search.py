
import sys

def rows_to_cols(grid: list[str]) -> list[str]:
  # assumes the grid is a square (len(rows) == len(cols))
  return ["".join([grid[j][i] for j in range(len(grid))]) for i in range(len(grid))]


def walk_down(pos: tuple[int, int], grid: list[str]) -> str:
  return "".join([
    grid[i + pos[0]][i + pos[1]]
    for i in range(len(grid))
    if 0 <= i + pos[0] < len(grid) and 0 <= i + pos[1] < len(grid)
  ])


def right_diagonals(grid: list[str]) -> list[str]:
  return (
    [walk_down((i, 0), grid) for i in range(len(grid))]
  + [walk_down((0, i), grid) for i in range(1, len(grid))]
  )
  

def walk_up(pos: tuple[int, int], grid: list[str]) -> str:
  return "".join([
    grid[pos[0] - i][pos[1] + i]
    for i in range(len(grid))
    if 0 <= pos[0] - i < len(grid) and 0 <= pos[1] + i < len(grid)
  ])


def left_diagonals(grid: list[str]) -> list[str]:
  return (
    [walk_up((len(grid) - 1 -i, 0), grid) for i in range(len(grid))]
  + [walk_up((len(grid) - 1, i), grid) for i in range(1, len(grid))]
  )


def search(grid: list[str]) -> int:
  return (
    sum([r.count("XMAS") + r.count("SAMX") for r in grid])
  + sum([r.count("XMAS") + r.count("SAMX") for r in rows_to_cols(grid)])
  + sum([r.count("XMAS") + r.count("SAMX") for r in right_diagonals(grid)])
  + sum([r.count("XMAS") + r.count("SAMX") for r in left_diagonals(grid)])
  )


def check_xmas(pos: tuple[int, int], grid: dict[tuple[int, int], str]) -> bool:
  neighbors = "".join([
    grid[(pos[0] + dr, pos[1] + dc)]
    for dr, dc in [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    if (pos[0] + dr, pos[1] + dc) in grid.keys()
  ])
  return len(neighbors) == 4 and neighbors in ["MSMS", "SSMM", "SMSM", "MMSS"]


def main():
  g = [line.strip() for line in open(sys.argv[1]).readlines()]
  xmas = search(g)
  print(xmas)

  grid = {}
  start = set()
  for r, row in enumerate(g):
    for c, col in enumerate(row):
      if col == "A":
        start.add((r, c))
      grid[(r, c)] = col

  xmas = sum([check_xmas(pos, grid) for pos in start])
  print(xmas)

if __name__ == "__main__":
  main()
