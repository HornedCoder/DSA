input_tuple = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)


daigonal_tuple = tuple(input_tuple[i][i] for i in range(len(input_tuple)))

print(daigonal_tuple)