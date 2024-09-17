string=input("")
string=string.strip("[]")
if string=="":
    print("")
else:
    string=string.split(",")
    string=[s.strip().strip("'\"") for s in string]
    common_prefix=string[0]
    for i in range(len(string)):
        if len(common_prefix)<=len(string[i]):
            n=len(common_prefix)
        else:
            n=len(string[i])
        for j in range(n):
            if common_prefix[j]!=string[i][j]:
                break
            elif j==n-1:
                j=j+1
            
        common_prefix=common_prefix[0:j]
    print(common_prefix)
            
        
    
    