def solution(s):
    s = list(s)
    arr = []
    i = 0
    while i < len(s):
        if s[i] == "z":
            arr.append('0')
            i = i + 4
            continue
        elif s[i] == "o":
            arr.append('1')
            i = i + 3
            continue
        elif s[i] == "t":
            if s[i+1] == "w":
                arr.append('2')
                i = i + 3
                continue
            else:
                arr.append('3') 
                i = i + 5
                continue
        elif s[i] == "f":
            if s[i+1] == "o":
                arr.append('4')
                i = i + 4
                continue
            else:
                arr.append('5')
                i = i + 4
                continue
        elif s[i] == "s":
            if s[i+1] == "i":
                arr.append('6')
                i = i + 3
                continue
            else:
                arr.append('7')
                i = i + 5
                continue
        elif s[i] == "e":
            arr.append('8')
            i = i + 5
            continue
        elif s[i] == "n":
            arr.append('9')
            i = i + 4
            continue
        else:
            arr.append(s[i])
            i += 1
    answer = ''.join(arr)
    return int(answer)