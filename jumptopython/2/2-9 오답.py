a = dict()
a
{}

#  >>> a = dict()
#  >>> a
#  {}

#  다음 중 오류가 발생하는 경우를 고르고, 그 이유를 설명해 보자.

#  1. a['name'] = 'python'
#    {name:python}이라 맞는듯?

#  2. a[('a',)] = 'python'
#    이게 오답???
# -> 이거 추가하는거라 가능한듯!!!

#  3. a[[1]] = 'python'
#    a[]의 1번째 값이라고 해석이 가능한가??
# -> 이거는 값을 바꾸는거라 불가능한듯!!

#  4. a[250] = 'python'
#    딕셔너리 a의 250번째 value값이 python이라 맞는듯?

a[[1]] = 'python'

# 오류가 발생하는 이유는 딕셔너리의 키로는 변하는(mutable) 값을 사용할 수 없기 때문이다.
# 위 예에서 키로 사용된 [1]은 리스트이므로 변하는 값이다.
# 다른 예에서 키로 사용된 문자열, 튜플, 숫자는 변하지 않는(immutable) 값이므로 딕셔너리의 키로 사용이 가능하다.