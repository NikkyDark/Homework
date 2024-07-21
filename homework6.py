my_dict = {'Nikita': 1993, 'Mary': 1995}
print(my_dict['Mary'])
my_dict['Victory'] = 2003
print(my_dict['Victory'])
my_dict.update({'Sobaka': 2018,
               'Sobaka_2': 2020})
print(my_dict)
del my_dict['Nikita']
print(my_dict.get('Nikita'))
print(my_dict)

my_set = {1, 'лето', 'зима', 2, 1, 2, (2, 1.5)}
my_set.add(5), my_set.add(7)
my_set.discard(1)
print(my_set)


