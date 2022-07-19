# 1. Mutable & Immutable

## mutable은 값이 변한다.
- List
- Set
- Dictionary
- Ndarray(NumPy의 배열)

## immutable은 값이 변하지 않는다.
- Number(숫자형)
- String(문자열)
- Tuple
- Range


# 2. Dictionary 만들기

## key 는 이름 , value 는 나이인 dictionary

dic = {'유지원':26, '홍영민':27, '김수형':28, '박용찬':29}


# 3. 평균 구하기
scores = [80, 89, 99, 83]

avg = sum(scores)/len(scores)
print(avg)


# 4. Dictionary 평균 구하기
dic = {'유지원':26, '홍영민':27, '김수형':28, '박용찬':29}

avg = sum(dic.values())/len(dic)
print(avg)


# 5. list

list = ['a', 'b', 'c', 'd']

#갯수
len(list) = 4

#리스트 안의 a의 개수
list.count('a')


num = [1, 20, 300, 4000]

#최댓값
max(num)

#최솟값
min(num)

#리스트 안의 1의 개수
num.count(1)


# 6. 단어 변환

#단어에서 'a'를 모두 제거
word = input()
word.replace('a', '')

#단어를 역순으로 뒤집기
word = input()
print(word[::-1])