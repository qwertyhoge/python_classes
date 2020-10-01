total = 0

print('abort with typing "end".')
while(True):
    num_as_str = input()
    if num_as_str == 'end':
        break

    total += int(num_as_str)

    print(total)
