import datetime

def time_it(func, numbers):
    start_t = datetime.datetime.now()
    for i in range(numbers):
        pass
    print(f' %s seconds of execution{datetime.datetime.now()-start_t}')

def list_comp(numbers):
    return [x**x for x in range(numbers)]

def list_for_loop(numbers):
    my_list = []
    for i in range(numbers):
           my_list.append(i**i)
    return my_list

print(list_for_loop(100000000))
time_it(list_comp, 100000000)
time_it(list_for_loop, 100000000)
