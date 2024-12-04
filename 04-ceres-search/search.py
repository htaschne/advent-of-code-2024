
import sys

def rows_to_cols(grid: list[str]) -> list[str]:
  # assumes the grid is a square (len(rows) == len(cols))
  return ["".join([grid[j][i] for j in range(len(grid))]) for i in range(len(grid))]


def extract_diags(grid: list[str]) -> list[str]:
  pass


def go_down(pos: tuple[int, int], grid: list[str]) -> list[str]:
  pass
      


def search(grid: list[str]) -> tuple[int, int, int]:
  h, v, d = 0, 0, 0
  h += sum([r.count("XMAS") + r.count("SAMX") for r in grid])
  v += sum([r.count("XMAS") + r.count("SAMX") for r in rows_to_cols(grid)])

  # d += sum([r.count("XMAS") + r.count("SAMX") for r in d1])

  

  return h, v, d

def main():
  g = [line.strip() for line in open(sys.argv[1]).readlines()]
  h, v, d = search(g)
  print(h + v + d)




if __name__ == "__main__":
  main()