immutable_var = (1, 2, 3, 'a', 'b')
print(immutable_var)
print(type(immutable_var))
# immutable_var[0] = 2 - нельзя изменить потому что кортэж неизменяемая упорядоченная коллекция
mutable_list = [1, 2, 'a','b', 'Mod']
mutable_list[0] = 4
mutable_list[-1] = 'hello'
print(mutable_list)
print(type(mutable_list))
