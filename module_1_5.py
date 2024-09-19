immuteble_var = ('name', 2, True)
print(immuteble_var)
print(type(immuteble_var))
#immuteble_var[2] = False  #Кортежи в Python являются неизменяемыми структурами данных, поэтому попытка изменить элемент кортежа не даст ожидаемого результата.
muteble_list = [10, 20,'Man','Salt', False]
print(muteble_list)
muteble_list[0] = 15
muteble_list[2] = 'Woman'
muteble_list[4] = True
print(muteble_list)