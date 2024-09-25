N=int(input(""))
M=int(input(""))
if N==M:
    a=N
    b=M
elif N>M:
    a=N
    b=M
else:
    a=M
    b=N
r=1
while r!=0:
    r=a%b
    a=b
    b=r
gcd=a
lcm=int((N*M)/gcd)
print(lcm)

    
