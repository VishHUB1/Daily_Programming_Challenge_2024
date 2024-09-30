def first_element(arr, k):
    count_dict = {}
    for num in arr:
        count_dict[num] = count_dict.get(num, 0) + 1
    for num in arr:
        if count_dict[num] == k:
            return num
    return -1
arr = list(map(int, input().strip("[]").split(",")))
k = int(input())

print(first_element(arr, k))
