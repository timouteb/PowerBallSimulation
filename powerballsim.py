from itertools import count
from time import perf_counter
from datetime import datetime
from random import sample, randint

pool = range(1,70)

def generate():
    return tuple(sorted(sample(pool, 5))), randint(1, 26)

if __name__ == '__main__':
    print('  #  |       Start Time       |   Winning Numbers    |      Number of Guesses   |   Time Taken   |        End Time      ')
    print('------------------------------------------------------------------------------------------------------------------------')
    for z in count(1):

    # Select winning number

        goal = generate()

        whitetuple = goal[0]

        white = (f'{whitetuple[0]:>02} {whitetuple[1]:>02} {whitetuple[2]:>02} {whitetuple[3]:>02} {whitetuple[4]:>02} ')
        pb = (f'{goal[1]:>02}')

        
        print(f'{z:>3}  |  {datetime.now().strftime("%m/%d/%Y, %H:%M:%S")}  |  {white} {pb}  |    ', end='', flush=True)

    # Start Timer

        start=perf_counter()

    # Try until a match is found. Show number of guesses and time taken

        for i in count(1):
            if generate() == goal:
                print(f'{i:>12,} guesses  |  {round(perf_counter() - start):>4} seconds  |  {datetime.now().strftime("%m/%d/%Y, %H:%M:%S")}')
                break