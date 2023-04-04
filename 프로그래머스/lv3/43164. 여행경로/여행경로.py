def dfs(airport, start, answer):
    while airport[start]:
        dfs(airport, airport[start].pop(0), answer)
        
    if not airport[start]:
        answer.append(start)
        return
    

    

def solution(tickets):
    airport = {}
    for i in tickets:
        depart, arrival = i
        airport[depart] = []
        airport[arrival] = []
    
    for i in tickets:
        depart, arrival = i
        airport[depart].append(arrival)
   
    for i in airport:
        airport[i].sort()
        
    print(airport)
    answer = []
    dfs(airport, "ICN", answer)

    return answer[::-1]