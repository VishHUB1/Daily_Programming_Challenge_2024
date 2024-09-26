N=int(input())
import math as m
count=0
for i in range(1,int(m.sqrt(N)+1)):
    if N%i==0:
        if i==N//i:
            count+=1
        else:
            count+=2
print(count)