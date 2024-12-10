
import sys

def main():
  disk = list(open(sys.argv[1]).readline().strip())
  parsed = {}
  file = True
  i, id = 0, 0
  files, gaps = [], []
  for c in disk:
    if file:
      for _ in range(int(c)):
        parsed[i] = str(id)
        i += 1
      files.append((i - int(c), id, int(c)))
      id += 1
    else:
      for _ in range(int(c)):
        parsed[i] = "."
        i += 1
      gaps.append((i - int(c), int(c)))
    file = not file

  lo, hi = 0, i - 1
  while lo < hi:
    if parsed[lo] == ".":
      while parsed[hi] == ".":
        hi -= 1
      parsed[lo], parsed[hi] = parsed[hi], parsed[lo]
      hi -= 1
    lo += 1

  # TODO: this hack is to swap the last two blocks
  # parsed[50263], parsed[50264] = parsed[50264], parsed[50263]
  acc = sum([int(parsed[j]) * j for j in range(i) if parsed[j] != "."])
  print(acc)

if __name__ == "__main__":
  main()
