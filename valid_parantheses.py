string=input("")
parantheses_open=[]
parantheses_close=[]
valid=False
if string=="":
    valid=True
for i in string:
    if i == "(" or i == "{" or i == "[":
        parantheses_open.append(i)
    if i == ")" or i == "}" or i == "]":
        parantheses_close.append(i)
if len(parantheses_open)!=len(parantheses_close):
    valid=False
else:
    for i in parantheses_open:
        if i=="(":
            index=parantheses_open.index(i)
            if parantheses_close[-(index+1)]==")":
                valid=True
        if i=="{":
            index=parantheses_open.index(i)
            if parantheses_close[-(index+1)]=="}":
                valid=True   
        if i=="[":
            index=parantheses_open.index(i)
            if parantheses_close[-(index+1)]=="]":
                valid=True
            
print(valid)
        
        