#!/usr/bin/env python3

import sys

from functools import cmp_to_key
from collections import defaultdict


def valid(page: list[str]) -> bool:
  global before
  for i, c in enumerate(page):
    for j in range(i + 1, len(page)):
      if page[j] in before[c]:
        return False
  return True


def page_compare(p1: str, p2: str) -> int:
  global before
  if p1 in before[p2]:
    return -1
  elif p2 in before[p1]:
    return 1
  else:
    return -1


def main():
  global before
  compare_page = cmp_to_key(page_compare)
  update = open(sys.argv[1]).read().strip().split("\n\n")

  rules = update[0].split("\n")
  for r in rules:
    v = r.split("|")
    before[v[1]].append(v[0])

  pages = [line.split(",") for line in update[1].split("\n")]

  valids = list(filter(lambda x: valid(x), pages))
  acc = sum([int(p[len(p) // 2]) for p in valids])
  print(acc)

  invalids = [sorted(p, key=compare_page) for p in filter(lambda x: not valid(x), pages)]
  acc = sum([int(p[len(p) // 2]) for p in invalids])
  print(acc)


before = defaultdict(list) 
if __name__ == "__main__":
  main()
