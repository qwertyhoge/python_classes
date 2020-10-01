num_f = 3.8
print('num_f: {}'.format(num_f))
print('num_f to int: {}'.format(int(num_f)))

num_i = 8
print('num_i: {}'.format(num_i))
print('num_i to float: {}'.format(float(num_f)))

num_s = '255'
print('num_s: {}'.format(num_s))
print('num_s to int: {}'.format(int(num_s)))

# error
# print('num_s + 100: {}'.format(num_s + 100))
print('num_s to int + 100: {}'.format(int(num_s) + 100))

# error
# print('num_i + num_s: {}'.format(num_i + num_s))
print('num_i to str + num_s: {}'.format(str(num_i) + num_s))