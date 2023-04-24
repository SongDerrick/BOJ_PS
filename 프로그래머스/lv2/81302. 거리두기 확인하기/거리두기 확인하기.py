def solution(places):
    answer = []
    for place in places:
        
        # 대기실 분리 
        graph = [[] for _ in range(5)]
        person = []
        flag = True
        for idx, j in enumerate(place): # 동일 대기실
            for k in range(5):
                graph[idx].append(j[k])
                if j[k] == 'P':
                    person.append((k, idx))
        
        print(graph)
        for i in person:
            if flag == False:
                break
                
            for j in person:
                if i == j:
                    continue
                matdist = abs(i[0]-j[0]) + abs(i[1]-j[1])
                if matdist <= 2:
                    # 4가지 케이스
                    print(i, j) 
                    if matdist == 1:
                        flag = False
                        break
                    
                    if i[1] == j[1]: # y 좌표 동일
                        if graph[i[1]][min(i[0],j[0])+1] == 'O':
                            flag = False
                            break
                    elif i[0] == j[0]: # x 좌표 동일
                        if graph[min(i[1],j[1])+1][i[0]] == 'O':
                            print("여기로 탈출")
                            flag = False
                            break
                    elif abs(i[0]-j[0]) == 1 and abs(i[1]-j[1]) == 1:
                        if graph[i[1]][j[0]] == 'O' or graph[j[1]][i[0]] == 'O':
                            print("dia")
                            flag = False
                            break


        if flag == True:
            answer.append(1)
        else:
            answer.append(0)
                            
    return answer