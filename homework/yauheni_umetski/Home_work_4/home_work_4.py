list_value = [1, 'two', 3, 'four', 5, 'six', 7, 'eight', 9, False, False, 0, 9, 1]
tuple_value = ('one', 2, 'three', 4, 'five', 6, 'seven', 8, 'nine', True)
set_value = set(list_value)
dict_value = {'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15}

my_dict = {'tuple': tuple_value, 'set': set_value, 'dict': dict_value, 'list': list_value}

print(my_dict['tuple'][-1])

my_dict['list'].append([])
my_dict['list'].pop(1)

my_dict['dict']["('i am a tuple',)"] = 12
del my_dict['dict']['eleven']

my_dict['set'].add(1234)
my_dict['set'].remove(False)

print(my_dict)