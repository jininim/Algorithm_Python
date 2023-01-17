s = "3people unFollowed me"
s = s.lower()
s = list(s.split(" "))

for i in range(len(s)):
    s[i] = s[i].capitalize()

print(" ".join(i for i in s))
