def print_params(a = 1, b = 'Hello', c = True):

    print(a,b,c)


values_list = [1,'a', False]

values_dict = {'a': 9, 'b': 'Hello', 'c': False}

values_list_2 = [65.37, 'hello']

print_params()
print_params(b = 25)
print_params(c = [1,2,3])
print_params(*values_list)
print_params(**values_dict )
print_params(*values_list_2, 42)