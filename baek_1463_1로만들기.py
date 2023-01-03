# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 19:19:29 2023

@author: 기원
"""

x = int(input())

d = [0]*30001
#print(d)


for i in range(2, x+1): #bottom up
    # 1을뺀다,
    d[i] = d[i-1]+1
    # x가 2로 나누어 떨어지면,2로 나눈다
    if i % 2 ==0:
        d[i] = min(d[i], d[i//2]+1)
    # x가 3으로 나누어떨어지면 3으로 나눈다
    if i % 3 ==0:
        d[i] = min(d[i], d[i//3]+1)
        
print(d[x])

'''
[ 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #리스트 요소 : 연산횟수
  ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ 
  0 1 2 3 4 5 6 7 8 9 10 11 12 13 연산 결과값
  

min --> 연산 결과값 i 까지 도달하는데 필요한 최소 연산횟수

1 --> 1을 뺐을경우(연산횟수 +1) --> 2 #역순
1 --> 2를 나눴을경우(연산횟수 +1)
1 --> 3를 나눴을경우 (연산횟수 +1)


'''

'''
ex) 10
[0 0 0 0 0 0 0 0 0 0 0 0]
[0 0 1 0 0 0 0 0 0 0 0 0 ]
[0 0 1 2 0 0 0 0 0 0 0 0 ]
[0 0 1 1 0 0 0 0 0 0 0 0 ]
[0 0 1 0 0 0 0 0 0 0 0 0 ]
[0 0 1 0 0 0 0 0 0 0 0 0 ]
[0 0 1 0 0 0 0 0 0 0 0 0 ]
[0 0 1 0 0 0 0 0 0 0 0 0 ]




'''