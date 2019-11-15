from random import getrandbits, randint

sick_days = randint(0, 10)

print(sick_days)
calling_in_sick = False

while not calling_in_sick and sick_days > 0:
    actually_sick = bool(getrandbits(1))
    kinda_sick = bool(getrandbits(1))
    dont_feel_like_it = bool(getrandbits(1))
    if actually_sick and sick_days > 0:
        calling_in_sick = True
        sick_days -= 1
    elif kinda_sick and dont_feel_like_it:
        calling_in_sick = True
        sick_days -= 1

    print(f'Are you sick : {calling_in_sick}')

else:
    print(f'It remain {sick_days} days of sickeness')