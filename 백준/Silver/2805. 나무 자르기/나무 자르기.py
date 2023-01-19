n, m = map(int, input().split())
heights = list(map(int, input().split()))
result = 0
start = 0
end = max(heights)
#1 ---------------------------
while (start + 1 < end):
    total = 0
    mid = (start + end) // 2
    for height in heights:
        if height > mid:
            total += height - mid

    if total < m:
        end = mid 

    else:
        start = mid 

print(start)