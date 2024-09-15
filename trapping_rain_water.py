arr = input("")
arr = list(map(int, arr.strip("[]").split(",")))
water = 0
left, right = 0, len(arr) - 1
left_max, right_max = arr[left], arr[right]
while left < right:
    if arr[left] < arr[right]:
        if arr[left] >= left_max:
            left_max = arr[left]
        else:
            water += left_max - arr[left]
        left += 1
    else:
        if arr[right] >= right_max:
            right_max = arr[right]
        else:
            water += right_max - arr[right]
        right -= 1
    print(water)
print(water)