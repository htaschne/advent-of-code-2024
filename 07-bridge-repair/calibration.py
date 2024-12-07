
import sys

def check(result: int, operands: list[int], acc: int, idx: int = 1) -> bool:
  if idx == len(operands) - 1:
    return (
      result == acc + operands[idx]
      or result == acc * operands[idx]
      or result == int(str(acc) + str(operands[idx]))
    )

  curr = operands[idx]
  if acc == 0:
    return check(result, operands, idx + 1, curr)

  plus = check(result, operands, acc + curr, idx + 1)
  mult = check(result, operands, acc * curr, idx + 1)
  conc = check(result, operands, int(str(acc) + str(curr)), idx + 1)
  return plus or mult or conc


def main():
  acc = 0
  for line in open(sys.argv[1]).readlines():
    x = line.strip().split(": ")
    result = int(x[0])
    operands = list(map(int, x[1].split(" ")))
    if check(result, operands, operands[0]):
      acc += result
  print(acc)


if __name__ == "__main__":
  main()
