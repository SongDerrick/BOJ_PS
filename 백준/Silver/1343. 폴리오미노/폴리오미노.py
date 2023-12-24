# 10448 폴리오미노

board = str(input())
splittedBoard = board.split(".")
possibility = True
result = []


def checkEmpty(n):
  if n == "":
    return True
  else:
    return False


temp = list(map(checkEmpty, splittedBoard))

for i in splittedBoard:
  noOfA = (len(i) // 4) * 4
  noOfB = ((len(i) - noOfA) // 2) * 2

  # print(i, noOfA, noOfB)
  if len(i) % 4 == 0:
    result.append(str('A' * noOfA))
  elif len(i) % 2 == 0:
    result.append(str('A' * noOfA + 'B' * noOfB))
  else:
    possibility = False
    break

if possibility:
  for i in range(len(result)):
    if result[i] == "":
      if i == len(result) - 1:
        break
      print(".", end="")
    elif i == len(result) - 1:
      if result[i] != "":
        print(result[i], end="")
    else:
      print(result[i], end=".")
else:
  print(-1)
