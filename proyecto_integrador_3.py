import os
from readchar import readkey, key

n = 0
while n < 50:
        k = readkey()
        if k == "n":
            n += 1
            os.system('cls' if os.name=='nt' else 'clear')
            print(n)

            