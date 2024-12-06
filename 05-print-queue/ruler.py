#!/usr/bin/env python3


import sys

from collections import defaultdict

def valid(page: list[str], before: dict[str, list[str]]) -> bool:
    for i, c in enumerate(page):
        for j in range(i + 1, len(page)):
            if page[j] in before[c]:
                return False
    return True


def main():
    update = open(sys.argv[1]).read().strip().split("\n\n")

    rules = update[0].split("\n")
    before, after = defaultdict(list), defaultdict(list)
    for r in rules:
        v = r.split("|")
        after[v[0]].append(v[1])
        before[v[1]].append(v[0])

    pages = [line.split(",") for line in update[1].split("\n")]
    valids = list(filter(lambda x: valid(x, before), pages))
    acc = sum([int(p[len(p)//2]) for p in valids])
    print(acc)



if __name__ == "__main__":
    main()
