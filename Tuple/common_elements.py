tuple1 = (1, 2, 3, 4, 5)
tuple2 = (4, 5, 6, 7, 8)

newt = tuple(tuple1[i] for i in range(len(tuple1)) if tuple1[i] in tuple2)

print(newt)