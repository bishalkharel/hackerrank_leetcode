import re

(n,m)=map(int,input().rstrip().split())
 
 # provide the shape of our matrix
 # we can also do
 ## n=7
 ## m=8

# create a empty list to store our elements 

matrix=[]

for _ in range(n):
    matrix.append(input())

value='' # for our undecoded string

for k in range(m): # selects letters
    for i in range(n): # selects words in a list:
        value+=matrix[i][k]

print(re.sub(r'\b[^a-zA-Z0-9]+\b',r' ',value))




