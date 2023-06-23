def solution(my_string, overwrite_string, s):
    a = my_string[:s]+ overwrite_string
    print(len(a))
    return my_string[:s]+ overwrite_string+ my_string[len(a):]