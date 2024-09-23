string=input()
max_length=0
for i in range(len(string)):
    for j in range(i+1,len(string)+1):
        sub_string=string[i:j]
        length=len(sub_string)
        char_ref=[]
        count=0
        for char in sub_string:
            if char not in char_ref:
                char_ref.append(char)
                count+=1
        if count==length and length>max_length:
            max_length=length
print(max_length)