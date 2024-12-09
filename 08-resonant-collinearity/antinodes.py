import sys

from collections import defaultdict

Grid = dict[tuple[int, int], str]


def ressonate(
  a: tuple[int, int], b: tuple[int, int], mr: int, mc: int
) -> list[tuple[int, int]]:
  antinodes = []

  c = (b[0] - a[0], b[1] - a[1])
  lo = (a[0] - c[0], a[1] - c[1])
  hi = (b[0] + c[0], b[1] + c[1])

  while 0 <= lo[0] <= mr and 0 <= lo[1] <= mc:
    antinodes.append(lo)
    lo = (lo[0] - c[0], lo[1] - c[1])

  while 0 <= hi[0] <= mr and 0 <= hi[1] <= mc:
    antinodes.append(hi)
    hi = (hi[0] + c[0], hi[1] + c[1])

  return antinodes


def main():
  anthenas = defaultdict(list)
  g: Grid = {}
  mr, mc = 0, 0
  for r, line in enumerate(open(sys.argv[1]).readlines()):
    for c, col in enumerate(line.strip()):
      if col != ".":
        anthenas[col].append((r, c))
      g[(r, c)] = col
      mr, mc = max(r, mr), max(c, mc)

  antinodes = set()
  for _, locations in anthenas.items():
    for i in range(len(locations)):
      for j in range(i + 1, len(locations)):
        for antinode in ressonate(locations[i], locations[j], mr, mc):
          antinodes.add(antinode)
      antinodes.add(locations[i])

  print(len(antinodes))


if __name__ == "__main__":
  main()
