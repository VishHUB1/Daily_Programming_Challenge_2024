N=input()
N=list(N.split(" "))
Exp=[]
for i in N:
    Exp.append(i)
    if i=="+":
        temp=int(Exp[-3])+int(Exp[-2])
        Exp.pop(-1)
        Exp.pop(-1)
        Exp.append(temp)
    elif i=="-":
        temp=int(Exp[-3])-int(Exp[-2])
        Exp.pop(-1)
        Exp.pop(-1)
        Exp.append(temp)
    elif i=="*":
        temp=int(Exp[-3])*int(Exp[-2])
        Exp.pop(-1)
        Exp.pop(-1)
        Exp.append(temp)
    elif i=="/":
        temp=int(int(Exp[-3])//int(Exp[-2]))
        Exp.pop(-1)
        Exp.pop(-1)
        Exp.append(temp)
print(Exp[-1])
        