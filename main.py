my_dict = {'bread': (5, 2.3),
           'milk': (2, 3.4)}

my_tuple = ('bread', 'milk')
def my_func(**kwargs):
    sum=0
    for i, j in kwargs.items():
     sum +=j[0]
    return sum

t = my_func(**my_dict)

print(t)


def print_arg_kwarg(*args, **kwargs):
    print(args)
    print(kwargs)



print_arg_kwarg(*my_tuple,**my_dict)
