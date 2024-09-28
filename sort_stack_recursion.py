def insert(stack, element):
    if len(stack) == 0 or stack[-1] <= element:
        stack.append(element)
    else:
        temp = stack.pop()
        insert(stack, element)
        stack.append(temp)

def sort_stack(stack):
    if len(stack) > 0:
        temp = stack.pop()
        sort_stack(stack)
        insert(stack, temp)

stack=input()
if stack=="[]":
    print("[]")
else:
    stack=list(map(int,stack.strip("[]").split(",")))
    sort_stack(stack)
    print(stack)


