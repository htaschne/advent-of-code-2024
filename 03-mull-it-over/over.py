
import sys
import re


def main():
  pat = r'mul\((\d+),(\d+)\)'

  acc = 0
  for line in open(sys.argv[1]).readlines():
    mm = re.findall(pat, line.strip())
    for m in mm:
      acc += int(m[0]) * int(m[1])
  print(acc)



if __name__ == "__main__":
  main()