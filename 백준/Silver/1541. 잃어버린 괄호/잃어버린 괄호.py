temp = input()
numbers = []
plusminus = []
count = 0
temp2 = 0
i = 0


while i < len(temp):
    if temp[i] == '+' or temp[i] == '-':
        plusminus.append(temp[i])
        for j in range(1, count+1):
            temp2 = temp2 + int(temp[i-j]) * pow(10,j-1)
        count = 0
        numbers.append(temp2)
        temp2 = 0
    elif i == len(temp)-1:
        count += 1
        for j in range(count):
            temp2 = temp2 + int(temp[i-j]) * pow(10,j)
        numbers.append(temp2)
    else:
        count += 1
    
    i = i + 1    

#print(numbers)
#print(plusminus)

j = 0
tempm = 0
paren = []

while True:
    
    if j >= len(plusminus):
        break
        
    if plusminus[j] == '-':
        while True:
            if j >= len(plusminus):
                break
            elif plusminus[j] == '+':
                tempm = tempm - numbers[j+1]
                paren.append(numbers[j+1])
                j += 1
            else:
                tempm = tempm - numbers[j+1]
                paren.append(numbers[j+1])
                j += 1   
    j += 1

#print(paren)
#print(numbers)
for i in paren:
    numbers.remove(i)
    
print(sum(numbers)+tempm)
