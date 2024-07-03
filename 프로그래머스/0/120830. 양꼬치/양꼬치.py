def solution(n, k):
    answer = 0
    
    yang = 12000*n
    drink = 2000*k
    service = 2000*(n//10)
    
    answer = yang+drink-service
    return answer