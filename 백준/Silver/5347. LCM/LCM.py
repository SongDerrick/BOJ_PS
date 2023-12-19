T = int(input())

target = []


def lcd(a, b):
  temp = 1

  if a > b:
    pivot = a
  else:
    pivot = b


# print(pivot)

  for i in range(1, pivot + 1):
    # print("i", i)

    if a % i == 0 and b % i == 0:
      temp = i

    # print("temp", temp)

  return temp

for _ in range(T):
  A, B = map(int, input().split(" "))
  target.append([A, B])

for i in range(T):
  temp = lcd(target[i][0], target[i][1])
  print(int(temp * target[i][0] / temp * target[i][1] / temp))
