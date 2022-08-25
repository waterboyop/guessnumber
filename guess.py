import random
num = random.randint(1,100)
time = 0
while True:
    num_g = int(input('Please input your number for guess:'))
    time = time + 1
    if num_g == num:
        print('You guess the correct number', num, 'Total for', time, 'times')
        break
    elif num_g > num:
        print('Your number is higher than answer!!')
    else:
        print('Your number is lower than answer!!')


    