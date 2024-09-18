strs=input()
strs=[s.strip().strip('"\'') for s in strs.strip("[]").split(",")]
def quicksort(word):
    if len(word) <= 1:
        return word
    else:
        pivot = word[-1]
        smaller = [value for value in word[:-1] if value <= pivot]
        greater = [value for value in word[:-1] if value > pivot]
        return quicksort(smaller) + [pivot] + quicksort(greater)
words=[]
anagrams_sets=[]
for word in strs:
    word=[ord(char) for char in word]
    word=quicksort(word)
    words.append(word)
checked=[]
for i in range(len(words)):
    if words[i] not in checked:
        count=0
        anagrams=[]
        for j in range(len(words)):
            if words[j]==words[i]:
                anagrams.append(strs[j])
        anagrams_sets.append(anagrams)
        checked.append(words[i])
print(anagrams_sets)
    
