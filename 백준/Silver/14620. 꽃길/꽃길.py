# 14620 꽃길

N = int(input())

land = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def check_in_land(x, y):
  for i in range(4):
    if x + dx[i] < 0 or y + dy[i] < 0 or x + dx[i] > N - 1 or y + dy[i] > N - 1:
      return False

  return True


def calculate_land_money(ax, ay, bx, by, cx, cy):
  total = land[ay][ax] + land[by][bx] + land[cy][cx]
  for i in range(4):
    total += land[ay + dy[i]][ax + dx[i]]
    total += land[by + dy[i]][bx + dx[i]]
    total += land[cy + dy[i]][cx + dx[i]]
  return total


def check_flowers_alive(ax, ay, bx, by, cx, cy):
  if (ax - bx)**2 + (ay - by)**2 <= 4:
    return False

  # if (ax - bx) == 0 or (ay - by) == 2:
  #   return False

  # if (ax - bx) == 2 or (ay - by) == 0:
  #   return False

  if (ax - cx)**2 + (ay - cy)**2 <= 4:
    return False

  # if (ax - cx) == 0 or (ay - cy) == 2:
  #   return False

  # if (ax - cx) == 2 or (ay - cy) == 0:
  #   return False

  if (bx - cx)**2 + (by - cy)**2 <= 4:
    return False

  # if (bx - cx) == 0 or (by - cy) == 2:
  #   return False

  # if (bx - cx) == 2 or (by - cy) == 0:
  #   return False

  return True


minMoney = 10e9
for _ in range(N):
  land.append(list(map(int, input().split(" "))))

for ax in range(N):
  for ay in range(N):
    if check_in_land(ax, ay):
      for bx in range(N):
        for by in range(N):
          if check_in_land(bx, by):
            for cx in range(N):
              for cy in range(N):
                if check_in_land(cx, cy) and check_flowers_alive(
                    ax, ay, bx, by, cx, cy):

                  currMoney = calculate_land_money(ax, ay, bx, by, cx, cy)
                  # print(ax, ay, bx, by, cx, cy)
                  # print("돈", currMoney)
                  if minMoney > currMoney:
                    minMoney = currMoney

print(minMoney)
