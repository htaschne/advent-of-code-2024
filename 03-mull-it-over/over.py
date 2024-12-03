
import re
import sys


def main():
  pat = r'mul\((\d+),(\d+)\)'

  acc = 0
  for line in open(sys.argv[1]).readlines():
    mm = re.findall(pat, line.strip())
    acc += sum([int(m[0]) * int(m[1])] for m in mm)
  print(acc)


if __name__ == "__main__":
  main()