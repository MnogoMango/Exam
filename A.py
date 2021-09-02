## -*- coding: utf-8 -*-
# input = open('C:\Users\danii\Desktop\Exam\win\A', 'r')
# matrix = input



f = input()

n = int(f)

matr = []

for i in range(n):
    matr += input().split(' ')

for i in range(len(matr)):
    matr[i] = int(matr[i])

result = 0

for i in range(0, len(matr), n+1):
    result += matr[i]

print(result)
