def solution(my_string):
    answer = ''
    
    for i in range(0, len(my_string)):
        if my_string[i].isupper():
            answer += my_string[i].lower()
        elif my_string[i].islower():
            answer += my_string[i].upper()
            
    return answer