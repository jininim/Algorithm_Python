# def solution(number, k):
#     arr = []
#     for i in number:
#         while arr and k > 0 and arr[-1] < i:
#             arr.pop()
#             k -= 1
#         arr.append(i)
#     answer = ''.join(i for i in arr)
#     return answer
#
#
# print(solution("4177252841", 4))
arr = "-1 -2 -3 -4 1 2 3 4"
a = list(map(int,arr.split(' ')))
a.sort()
print(a[0],a[-1])