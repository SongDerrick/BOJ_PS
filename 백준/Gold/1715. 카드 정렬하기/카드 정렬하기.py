
import sys
import heapq
from collections import deque
input = sys.stdin.readline
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n = int(input())
    cards = []
    result = []
    for _ in range(n):
        card = int(input())
        heapq.heappush(cards, card)

    if n == 1:
        print('0')
    else:
        while len(cards) > 2:
            #temp = cards.popleft() + cards.popleft()
            temp = heapq.heappop(cards) + heapq.heappop(cards)
            #print(temp)
            #print(temp)
            result.append(temp)
            for idx, card in enumerate(cards):
                if card > temp:
                    i = idx
                    break
                else:
                    i = len(cards)
            #cards.insert(i,temp)
            heapq.heappush(cards, temp)
            #print(cards)

        #print(sum(cards))
        result.extend(cards)
        #print(result)

        print(sum(result))
