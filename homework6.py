my_dict={'Kat':1982, 'Max':1983, 'Sofiya':2009}
print('Dict:', my_dict)
a = my_dict.pop('Kat')
print(a)
print(my_dict.get('Irina'))
my_dict={'Kat':1982, 'Max':1983, 'Sofiya':2009}
del my_dict['Max']
print(my_dict)

my_set={1,2,3,4,2,3,4,True,'Привет'}
print(my_set)
my_set.add(5)
my_set.add('Пока')
my_set.discard(2)
print(my_set)