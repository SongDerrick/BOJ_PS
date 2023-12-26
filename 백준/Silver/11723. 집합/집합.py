# 11723 집합
import sys

M = int(sys.stdin.readline())

S = set()
for _ in range(M):
  userInput = sys.stdin.readline().strip()

  if (userInput == "all"):
    for i in range(1, 21):
      S.add(str(i))
  elif (userInput == "empty"):
    S = set()
  else:
    command, value = userInput.split(" ")
    if (command == "add"):
      S.add(value)
    elif (command == "remove"):
      S.discard(value)
    elif (command == "check"):
      if (value in S):
        print(1)
      else:
        print(0)
    elif (command == "toggle"):
      if (value in S):
        S.discard(value)
      else:
        S.add(value)
