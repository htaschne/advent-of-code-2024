
import sys


def check(level: list[int]) -> bool:
  incs = [(p - n) for p, n in zip(level, level[1:])]
  pos = all([x > 0 for x in incs])
  neg = all([x < 0 for x in incs])
  par = all([1 <= abs(x) <= 3 for x in incs])
  return (pos or neg) and par


def main():
  levels = [list(map(int, l.strip().split(" "))) for l in open(sys.argv[1]).readlines()]
  acc = sum([check(level) for level in levels])
  print(acc)

  acc = 0
  for level in levels:
    if check(level):
      acc += 1
    else:
      for i in range(len(level)):
        nl = level[:i] + level[i+1:]
        if check(nl):
          acc += 1
          break
  print(acc)


if __name__ == "__main__":
  main()