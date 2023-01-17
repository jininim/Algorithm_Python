s = "baabaa"
arr = list(s)

while len(arr) > 1:
    for i in range((len(arr)-1)):
        if arr[i] == arr[i+1]:
            del arr[i]
            del arr[i+1]
            break

if arr:
    print(0)
else:
    print(1)
