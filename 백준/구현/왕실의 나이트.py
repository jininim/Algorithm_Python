n = input()
cnt = 0
x = int(n[1])
if n[0] == 'a':
    y = 1
if n[0] == 'b':
    y = 2
if n[0] == 'c':
    y = 3
if n[0] == 'd':
    y = 4
if n[0] == 'e':
    y = 5
if n[0] == 'f':
    y = 6
if n[0] == 'g':
    y = 7
if n[0] == 'h':
    y = 8
step = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

for a, b in step:
    if 1 <= x + a <= 8 and 1 <= y + b <= 8:
        cnt += 1
print(cnt)