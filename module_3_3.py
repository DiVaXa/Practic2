def print_params(a=1, b='строка', c=True):
    print(a, b, c)
print_params()
print_params(b = 25)
print_params(c = [1,2,3])
values_list = [False, 2, 'текст']
values_dict = {'a':'ку-ку', 'b':False, 'c':6}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = ['solo', 155]
print_params(*values_list_2, 42)