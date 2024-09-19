my_dict = {"Лена": 1999, "Петя": 2001, "Слава": 1988}
print(my_dict["Лена"])
print(my_dict.get('Фиксик'))
print(my_dict)
my_dict.update({"Филипп": 2005, "Саша": 1944})
print(my_dict)
del my_dict ["Петя"]
print(my_dict)

my_set = {1,1,2,2,2,3,4,20.5, 'Cod', 'Dog', True, (1,2)}
print(my_set)
my_set.add(5)
my_set.add('Cat')
my_set.remove(1)
print(my_set)