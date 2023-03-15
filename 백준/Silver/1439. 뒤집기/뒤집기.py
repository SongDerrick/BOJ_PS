# 1439 뒤집기

s = input()

previous = s[0]
muntung = [0, 0]

for i in range(len(s)):
  if s[i] != previous:
    muntung[int(previous)] += 1
    previous = s[i]

  if i == len(s) - 1 and previous == s[i]:
    muntung[int(previous)] += 1

print(min(muntung))
