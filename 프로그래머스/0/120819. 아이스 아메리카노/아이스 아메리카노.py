def solution(money):
    answer = []
    ame = money // 5500
    ref = money % 5500
    
    answer = [ame, ref]
    
    return answer