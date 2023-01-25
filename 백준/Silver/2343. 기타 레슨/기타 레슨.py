# 2343 기타 레슨

# 이진 탐색 문제로 보입니다만....


N, M = map(int, input().split(" "))
target = list(map(int, input().split(" ")))

min_pivot = 1
max_pivot = sum(target)

#print(min_pivot, max_pivot)

start = min_pivot
end = max_pivot



while start <= end:
  
  
  mid = (start + end) // 2
  #print(start, end)
  #print(mid)
  result= [0]
  temp = 0
  count = M-1
  
  for i in range(N-1, -1, -1):
    
    if target[i] > mid:
      result[-1] = mid + 1
      break
    elif temp + target[i] > mid and count != 0:
      result.append(temp)
      count -= 1
      temp = target[i]
      if i == 0:
        result.append(temp)
    else:
      temp += target[i]
      if i == 0:
        result.append(temp)


  #print(result)
  
  
  if result[-1] <= mid:
    end = mid -1
    final = mid
  else:
    start = mid + 1
    final = start
    
print(final)