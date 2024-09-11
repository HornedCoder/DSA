from collections import deque

que = deque(maxlen = 3)
print(que)
'''This append is like enqueue function.'''
que.append(1)
que.append(2)
que.append(3)
print("The queue looks like this:",que)
print("We use append again and it pops the start of the que:")
que.append(4)
print("The new que after append que.append(4) looks like this:",que)
'''popleft() is like dqueue function.'''
print("We are going to dequeu element using popleft which is similar to dequeue.The popped element is:",que.popleft())
print("The queue looks like this after one popleft:",que)
'''clear is like delete all'''
que.clear()
print("The que after using clear:",que)