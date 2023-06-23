str = input()
answer = []
for i in str:
    if i.islower():
        answer.append(i.upper())
    elif i.isupper():
        answer.append(i.lower())
print(''.join(answer))