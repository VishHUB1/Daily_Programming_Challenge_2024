string=input()
palindromes=[];palindrome_lengths=[]
for i in range(len(string)):
    sub_string=""
    for j in range(i,len(string)):
        sub_string+=string[j]
        if sub_string==sub_string[::-1]:
            palindromes.append(sub_string)
            
max=0
for i in palindromes:
    if len(i)>max:
        max=len(i)
        longest_substring=i
print(longest_substring)
            
