
import sys

def rows_to_cols(grid: list[str]) -> list[str]:
  # assumes the grid is a square (len(rows) == len(cols))
  return ["".join([grid[j][i] for j in range(len(grid))]) for i in range(len(grid))]

def walk_down(pos: tuple[int, int], grid: list[str]) -> list[str]:
  row = []
  for i in range(len(grid)):
    if 0 <= i + pos[0] < len(grid) and 0 <= i + pos[1] < len(grid):
      row.append(grid[i + pos[0]][i + pos[1]])
  return "".join(row)


def right_diagonals(grid: list[str]) -> list[str]:
  rows = [walk_down((i, 0), grid) for i in range(1, len(grid))]
  cols = [walk_down((0, i), grid) for i in range(len(grid))]
  return rows + cols


def walk_up(pos: tuple[int, int], grid: list[str]) -> list[str]:
  row = []
  for i in range(len(grid)):
    if 0 <= pos[0] - i < len(grid) and 0 <= pos[1] + i < len(grid):
      row.append(grid[pos[0] - i][pos[1] + i])
  ret = "".join(row)
  return ret


def left_diagonals(grid: list[str]) -> list[str]:
  rows, cols = [], []
  rows = [walk_up((len(grid) - 1 -i, 0), grid) for i in range(1, len(grid))]
  cols = [walk_up((len(grid) - 1, i), grid) for i in range(len(grid))]
  ret = rows + cols
  return ret






def search(grid: list[str]) -> tuple[int, int, int]:
  h = sum([r.count("XMAS") + r.count("SAMX") for r in grid])
  v = sum([r.count("XMAS") + r.count("SAMX") for r in rows_to_cols(grid)])
  dr = sum([r.count("XMAS") + r.count("SAMX") for r in right_diagonals(grid)])
  dl = sum([r.count("XMAS") + r.count("SAMX") for r in left_diagonals(grid)])
  return h, v, dr + dl

def main():
  g = [line.strip() for line in open(sys.argv[1]).readlines()]
  h, v, d = search(g)
  print(h + v + d)



if __name__ == "__main__":
  main()