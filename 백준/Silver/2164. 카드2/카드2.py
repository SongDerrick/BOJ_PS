# 2164 카드2

from collections import deque

N = int(input())

card = deque([i for i in range(1, N + 1)])

while len(card) > 1:  # 카드 한 장 남을 때까지 반복
  card.popleft()  # 일단 가장 아래 카드 뺌
  card.append(card.popleft())  # 그 다음 카드 빼서 더함

print(card.pop())  # 마지막 남은 카드
