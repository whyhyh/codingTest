'''
def solution(my_string):
    answer = ''
    
    for i in range(len(my_string)):
        if ((my_string[i] != 'a')&(my_string[i] != 'e')&
            (my_string[i] != 'i')&(my_string[i] != 'o')&
            (my_string[i] != 'u')):
            #print(my_string[i])
            answer += my_string[i]
            
    return answer
'''
def solution(my_string):
    vowels = ['a','e','i','o','u']
    for vowel in vowels:
        my_string = my_string.replace(vowel, '')
    return my_string