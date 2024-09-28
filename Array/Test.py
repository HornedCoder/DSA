'''
print('Fukumean')

def f(value,values):
    value = 1
    values[0] = 44

t = 3
v = [1,2,3]

f(t,v)
print(t,v[0])
'''
stack = []
stack.append([2])
print(stack)
stack.append([3])
print(stack)
stack[-1].append(1)
print(stack)
stack.append(0)
print(stack)
a = [1,2,4]
print(a[-2::-1])