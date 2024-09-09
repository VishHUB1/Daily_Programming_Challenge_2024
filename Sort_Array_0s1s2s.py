arr=input()
if arr=='[]':
    print(arr)
else: 
    arr = list(map(int, arr.strip('[]').split(',')))
    count1=0;count2=0;count3=0
    for i in range(len(arr)):
        if arr[i]==0:
            count1+=1
        if arr[i]==1:
            count2+=1
        if arr[i]==2:
            count3+=1
    for i in range(count1):
        arr[i] = 0
    for i in range(count1, count1 + count2):
        arr[i] = 1
    for i in range(count1 + count2, count1 + count2 + count3):
        arr[i] = 2
    print(arr)