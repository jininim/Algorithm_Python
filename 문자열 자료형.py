# 사전 자료형 hash table
data = dict()
data['사과'] = 'apple'
data['바나나'] = 'banana'
#키,값 데이터만 담은 리스트
key_list = data.keys()
value_list = data.values() #값
print(key_list,value_list)

# 각 키에 따른 값을 하나씩 출력
for key in key_list:
    print(data[key])

# 집합 자료형 중복불가 , 순서없음
# 집합 자료형 초기화 방법
a = set([1,1,2,3,4,4,5])
b = {1,1,2,3,4,4,5}
a | b # 합집합
a & b # 교집합
a - b # 차집합
# 새로운 원소 추가 add 함수 사용
# 새로운 원소 여러 개 추가 update 함수 사용
# 특정한 값을 갖는 원소 삭제 remove 함수 사용용