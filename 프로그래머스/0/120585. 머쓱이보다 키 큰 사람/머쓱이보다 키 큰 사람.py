def solution(array, height):
    array.append(height)
    arr = sorted(array,reverse=True)
    return arr.index(height)