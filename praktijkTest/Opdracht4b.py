import datetime

def time_it(func, numbers):
    start_t = datetime.datetime.now()
    for i in range(numbers):
        pass
    print(f' %s seconds of execution: {datetime.datetime.now()-start_t}')


# build a list
def list_comp(numbers):
    return [(i*2 + 5) % 13 if i % 2 == 0 else (i*3 + 7) % 23 for i in range(numbers)]


# build a list with For loop
def list_for_loop(numbers):
    own_list = []
    for i in range(numbers):
        if i % 2 == 0:
            own_list.append( (i*2 + 5) % 13)
        else:
            own_list .append( (i*3 + 7) % 23)
    return own_list


number = 100000
print(list_comp(number))
time_it(list_comp, number)
print()
print(list_for_loop(number))
time_it(list_for_loop, number)




