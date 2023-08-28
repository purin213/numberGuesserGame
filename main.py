#import os
import sys
from random import randint

sys.stdout.buffer.write(b'Input your minimum number: ')
sys.stdout.flush()
minN = sys.stdin.readline()
sys.stdout.buffer.write(b'Now, input your maximum number: ')
sys.stdout.flush()
maxN = sys.stdin.readline()

randN = randint(int(minN),int(maxN))
#print(randN)

tries = 10;

while tries != 0:
    sys.stdout.buffer.write(b'Can you guess the random number? \n')
    sys.stdout.flush()
    guess = sys.stdin.readline()
    if randN == int(guess):
        sys.stdout.buffer.write(b'Great job, ') 
        break
    tries -= 1
    if tries != 0:
        sys.stdout.buffer.write(b'Wrong number, try again. ')

if tries == 0:
    sys.stdout.buffer.write(b'You ran out of tries! Better luck next time, ')

sys.stdout.buffer.write(b'Thank you for playing!')
sys.stdout.flush()

"""
#------------fix me----------
res = sys.stdin.readline()
print(res)
print(type(res))

match res:
    case 'y':
        os.execl(sys.executable, sys.executable, *sys.argv)
    case 'n':
        sys.exit("Thanks for playing")
    case _:
        sys.exit("Bad input, exiting program")
"""
