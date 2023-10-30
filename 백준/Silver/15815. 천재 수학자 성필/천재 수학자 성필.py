mylist = list(input())
stack = []

for i in mylist:
    if i == '+':
        num1 = stack.pop()
        num2 = stack.pop()
        stack.append(num1+num2)
    elif i == '-':
        num1 = stack.pop()
        num2 = stack.pop()
        stack.append(num2-num1)
    elif i == '*':
        num1 = stack.pop()
        num2 = stack.pop()
        stack.append(num1*num2)    
    elif i == '/':
        num1 = stack.pop()
        num2 = stack.pop()
        stack.append(num2//num1)  
    else :
        stack.append(int(i))

print(stack[0])