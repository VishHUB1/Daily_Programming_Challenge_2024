arr=input("")
arr=list(map(int,arr.strip("[]").split(",")))
subarrays=[]
for i in range(len(arr)):
    sum=0
    for j in range(i,len(arr)):
        sum+=arr[j]
        if sum==0:
            subarrays.append((i,j))
print(subarrays)
        
        