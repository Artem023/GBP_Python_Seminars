""" На столе лежат n монеток. Некоторые из них лежат вверх
решкой, а некоторые – гербом. Определите минимальное число
монеток, которые нужно перевернуть, чтобы все монетки были
повернуты вверх одной и той же стороной. Выведите минимальное
количество монет, которые нужно перевернуть. 
5 -> 1 0 1 1 0
2
"""
from random import randint as rnd

num_coins = int (input ("How much coins are on the table?: "))
heads_tails = [rnd(0, 1) for _ in range(num_coins)]
print(heads_tails)

# heads == 0; tails == 1
heads = 0
tails = 0     

for i in heads_tails:
    if i == 0:
        heads += 1
    else: 
        tails += 1
print(heads, tails)

index = 0

if heads < tails:
    for i in heads_tails:
        if i == 1:
            heads_tails[index] = 0
            index += 1
        else: index += 1
    print(f"Min = {heads} -> {heads_tails}")

else:
    for i in heads_tails:
        if i == 0:
            heads_tails[index] = 1
            index += 1
        else: index += 1
    print(f"Min = {tails} -> {heads_tails}")
