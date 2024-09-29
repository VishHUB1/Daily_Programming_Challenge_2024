def insert_at_bottom(stack, item):
    if len(stack) == 0:
        stack.append(item)
    else:
        temp = stack.pop()
        insert_at_bottom(stack, item)
        stack.append(temp)
def reverse_stack(stack):
    if len(stack) > 0:
        temp = stack.pop()
        reverse_stack(stack)
        insert_at_bottom(stack, temp)

stack = input()
if stack == "[]":
    print("[]")
else:
    stack = list(map(int, stack.strip("[]").split(",")))
    reverse_stack(stack)
    print(stack)
