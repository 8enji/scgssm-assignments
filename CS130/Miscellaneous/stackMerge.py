stack1 = []
stack2 = []
stack3 = []
stack4 = []

# append() function to push
# element in the stack
stack1.append(8)
stack1.append(9)
stack1.append(30)
stack1.append(56)
stack1.append(57)
stack1.append(90)
stack1.append(101)
stack1.append(105)

stack2.append(7)
stack2.append(11)
stack2.append(12)
stack2.append(45)
stack2.append(76)
stack2.append(89)


print('Initial stack')
print(stack1)
print(stack2)


def stackMerge(stack1,stack2):
    x = stack1.pop()
    y = stack2.pop()
    stack3 = []
    run = True
    run2 = True
    while(run):
        if x > y:
            stack3.append(x)
            try:
                x = stack1.pop()
            except:
                print('Empty')
                stack3.append(y)
                run = False
        else:
            stack3.append(y)
            try:
                y = stack2.pop()
            except:
                print('Empty')
                stack3.append(x)
                run = False
    return stack3

def getMax(stack):
    run = True
    stackTemp = stack.copy()
    max = stackTemp.pop()
    while(run):
        try:
            x = stackTemp.pop()
        except:
            run = False
        if x > max:
            max = x
    return max

print(stack2)
print(getMax(stack2))
print(stack2)
#print(stackMerge(stack1, stack2))

