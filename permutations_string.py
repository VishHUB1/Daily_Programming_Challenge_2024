def permutations(string,partial_permutation="",permutations_list=[]):
    if len(string)==0 and partial_permutation not in permutations_list:
        permutations_list.append(partial_permutation)
    else:
        for i in range (len(string)):
            new_permutation=partial_permutation+string[i]
            remaining=string[:i]+string[i+1:]
            permutations(remaining,new_permutation)
    return permutations_list
string=input("")
print(permutations(string))