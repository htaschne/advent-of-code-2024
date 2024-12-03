
import re
import sys


def main():
  pat = r"mul\((\d+),(\d+)\)"
  acc = sum(
    [
      sum([int(m[0]) * int(m[1]) for m in re.findall(pat, line.strip())])
      for line in open(sys.argv[1]).readlines()
    ]
  )

  print(acc)


if __name__ == "__main__":
  main()
