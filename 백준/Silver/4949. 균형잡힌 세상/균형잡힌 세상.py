big = []
result = []

while True:
    
    s1 = input()
    
    if s1 == '.':
        break
    
    for word in s1:
        #print(word)
        if word == '[':
            big.append('1')
        elif word == '(':
            big.append('2')
        elif word == ']':
            if len(big) != 0 and big[-1] == '1':
                big.pop()
            else:
                big.append('1')
                break


        elif word == ')':
            if len(big) != 0 and big[-1] == '2':
                big.pop()
            else:
                big.append('2')
                break

    if len(big) == 0: 
        result.append("yes")
    else:
        result.append("no")
        big = []

       
            
for i in range(len(result)):
    print(result[i])
    
