﻿# 변수 선언은 간단하다
a = 13
# 정수형 변수 선언 : 동적 타입 언어기 때문에 런타임에 타입 검사를 수행한다

# 타입은 어떻게 알 수 있을까
print(type(a))
# <class 'int'>라고 나온다

a = 3.5
# int가 담겼던 변수에 재할당
# 소수점이 포함된 숫자는 실수형으로 분류된다
# 파이썬에서 실수는 float만 사용한다
print(type(a))

a = 0.8e+15
# e 표기법
print(a)

# e 표기법을 사용하면 float형으로 저장된다
print(type(a))

a = 0x1f
# 16진수
print(a)

a = 0o14
# 8진수
print(a)

print(5 / 2)
# 일반적인 나눗셈. 몫은 무조건 float. true div라고 말함

print(5 // 2)
# 반올림하여 몫을 int로 반환, floor div라고 말함

print(5 ** 2)
# 제곱
