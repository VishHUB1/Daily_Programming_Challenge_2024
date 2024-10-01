arr=list(map(int,input().strip("[]").split(",")))
k=int(input())
size=len(arr)
max_elements=[]
for i in range(size+1-k):
    max=arr[i]
    for j in range(i,i+k):
        if arr[j] > max:
            max=arr[j]
    max_elements.append(max)
print(max_elements)

    