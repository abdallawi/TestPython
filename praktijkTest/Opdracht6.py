def list_manipulation(list, command, location, *args):
    if command == 'remove' and location == 'beginning':
        element = list[0]
        list.pop(0)
        print(element)
    elif  command == 'remove' and location == 'end':
        element = list[-1]
        list.pop(-1)
        print(element)
    elif command == 'add' and location == 'beginning':
        new_list = [*args]
        new_list.extend(list)
        print(new_list)
    elif command == 'add' and location == 'end':
        list.append(*args)
        print(list)


list_manipulation([1, 2, 3], 'remove', 'end')
list_manipulation([1, 2, 3], 'remove', 'beginning', 20)
list_manipulation([1, 2, 3], 'add', 'beginning', 20)
list_manipulation([1, 2, 3], 'add', 'end', 30)