import os
from readchar import readkey, key

def borrar_imprimir_terminal(num):
    os.system('cls' if os.name=='nt' else 'clear')
    print(num)
    
n = 0
while n < 50:
    k = readkey()
    if k == "n":
        n += 1
        borrar_imprimir_terminal(n)
