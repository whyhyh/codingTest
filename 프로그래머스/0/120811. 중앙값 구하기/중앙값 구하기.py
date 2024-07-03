def solution(array):
    answer = 0
    
    sort_list = sorted(array)
    
    array_len = len(array)
    tmp = array_len//2
    
    return sort_list[tmp]