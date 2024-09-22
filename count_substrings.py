string=input()
k=int(input())
total=0
for i in range(len(string)):
    for j in range(i+1,len(string)+1):
        sub_string=string[i:j]
        char=[]
        count=0
        for m in sub_string:
            if m not in char:
                count+=1
                char.append(m)
        if count==k:
            total+=1
print(total)