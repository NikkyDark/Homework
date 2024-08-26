def print_params(a=1, b='string', c=True):
    print(a, b, c)


print_params()
print_params('b')
print_params(1, 'c')
print_params(b=25), print_params(c=[1, 2, 3])

values_list = [1, 'b', True]
values_dict = {'a': 2.4, 'b': 'yo', 'c': [1 > 0]}

print_params(*values_list)
print_params(**values_dict)
# print_params(*values_list, **values_dict)??? в задании указано вывести вместе, но это не реально, потому как и там и
# там по 3 значения, а должно быть всего 3

values_list_2 = [4, 'ace']
print_params(*values_list_2, 42)
