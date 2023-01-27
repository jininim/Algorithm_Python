def solution(s):
    s = s.lower()
    cntp = 0
    cnty = 0
    for i in s:
        if i == "p":
            cntp +=1
        elif i == "y":
            cnty +=1
    if cntp == cnty or cntp ==0 and cnty ==0:
        return True
    else:
        return False
