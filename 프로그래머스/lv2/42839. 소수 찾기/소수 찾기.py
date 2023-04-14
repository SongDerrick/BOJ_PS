import itertools

def prime(f):
    if f == 1:
        return False
    
    for i in range(2, f):
        if f % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    for i in range(1, len(numbers)+1):
        temp = set(itertools.permutations(numbers, i))
        print(temp)
        
        
        for j in temp:
            f = ''
            for k in j:
                f += k
            print(f)
            if prime(int(f)) and f[0] != '0':
                answer += 1
                

    return answer