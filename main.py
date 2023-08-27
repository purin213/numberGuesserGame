import sys
from random import randint

sys.stdout.buffer.write(b'Input your minimum number: ')
sys.stdout.flush()
minN = sys.stdin.buffer.readline()
sys.stdout.buffer.write(b'Now, input your maximum number: ')
sys.stdout.flush()
maxN = sys.stdin.buffer.readline()
#------------fix me----------
randN = randint(int.from_bytes(minN, "little"), int.from_bytes(maxN, "little"))
print(randN)

tries = 10;

while tries != 0:
    sys.stdout.buffer.write(b'Now, can you guess the random number? \n')
    sys.stdout.flush()
    guess = sys.stdin.buffer.readline()
    if randN == guess:
        sys.stdout.buffer.write(b'Good job, care for another game? Yes/y No/n ')
        sys.stdout.flush()
        break
    tries -= 1

if tries == 0:
    sys.stdout.buffer.write(b'You ran out of tries! \n')
    sys.stdout.buffer.write(b'Better luck next time, care for another game? Yes/y No/n ')
    sys.stdout.flush()

#------------fix me----------
res = sys.stdin.buffer.readline()

match res:
    case 'y':
        os.execl(sys.executable, sys.executable, *sys.argv)
    case 'n':
        sys.exit("Thanks for playing")
    case _:
        sys.exit("Bad input, exiting program")
