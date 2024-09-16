string = input()
n = len(string)
start = 0
end = n - 1
while start < n and string[start] == ' ':
    start += 1
while end >= 0 and string[end] == ' ':
    end -= 1
words = []
i = start
while i <= end:
    while i <= end and string[i] == ' ':
        i += 1
    word_start = i
    while i <= end and string[i] != ' ':
        i += 1
    if word_start != i: 
        words.append(string[word_start:i])
for i in range(len(words) - 1, -1, -1):
    print(words[i], end=" ")
