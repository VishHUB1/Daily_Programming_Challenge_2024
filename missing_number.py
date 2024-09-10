arr=input("")
arr=list(map(int, arr.strip('[]').split(",")))
sum1 = int(((len(arr)+1)*(len(arr)+2))/2)
print(sum1- sum(arr))
        
