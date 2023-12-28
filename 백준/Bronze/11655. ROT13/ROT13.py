# 11655 ROT13

S = str(input())

for i in S:
  if ord('A') <= ord(i) <= ord('Z'):
    # 대문자 케이스
    if (ord(i) + 13 > ord('Z')):
      print(chr(ord(i) + 12 - ord('Z') + ord('A')), end="")
    else:
      print(chr(ord(i) + 13), end="")

  elif ord('a') <= ord(i) <= ord('z'):
    # 소문자 케이스
    if (ord(i) + 13 > ord('z')):
      print(chr(ord(i) + 12 - ord('z') + ord('a')), end="")
    else:
      print(chr(ord(i) + 13), end="")
  else:
    print(i, end="")
