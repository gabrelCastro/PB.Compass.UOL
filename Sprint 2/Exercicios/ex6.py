def my_map(lista,f):
    new_list = []
    for i in lista:
        new_list.append(f(i))
    return new_list;
    
print(my_map([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],lambda x : x**2))