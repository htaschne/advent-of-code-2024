
import sys

def fit(f, gaps):
  index, _, fsize = f

  # move whole files to the leftmost span of free space
  for i, (_, gstart, gsize) in enumerate(gaps):
    if gsize >= fsize:
      nsize = gsize - fsize
      nf = (index, gstart, fsize)
      if nsize > 0:
        ng = gaps[:i] + [(".", gstart + fsize, nsize)] + gaps[i + 1:]
      else:
        ng = gaps[:i] + gaps[i + 1:]
      return nf, ng

  return f, gaps


def main():
  disk = open(sys.argv[1]).read().strip()

  index = 0
  blocks = []
  length = 0
  for i, block in enumerate(disk):
    if i % 2 == 0: # File
      size = int(block)
      blocks.append((index, length, size))
      index += 1
      length += size

    else: # Free Space
      size = int(block)
      blocks.append((".", length, size))
      length += size

  files = [b for i, b in enumerate(blocks) if i % 2 == 0]
  gaps = [b for i, b in enumerate(blocks) if i % 2 != 0]

  # the rightmost file fills the leftmost gap that fits the whole file
  dfiles = []
  for f in reversed(files):
    nf, gaps = fit(f, gaps)
    dfiles.append(nf)
  
  # add the whole ranges for lookup
  final = {}
  for index, start, size in reversed(dfiles):
    for i in range(start, start + size):
      final[i] = index
  
  # Final disk after moving the files
  ret = ""
  for i in range(length):
    if i in final.keys():
      ret += str(final[i])
    else:
      ret += "."

  print(ret)
  acc = sum([final[i] * i for i in range(length) if i in final.keys()])
  print(acc)



if __name__ == "__main__":
  main()
