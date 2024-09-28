total = 0
count = 0

while True:
    inp = input('Enter a number: ')
    if inp == 'Done':
        break
    value = float(inp)
    total = total + value
    count = count + 1
    average = total/count


print('Average = ',average)
