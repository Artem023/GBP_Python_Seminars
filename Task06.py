""" 
Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
Вам требуется написать программу, которая проверяет счастливость билета.
"""
try: 
    while True:
        num = int (input ("Type a ticket number: "))
        count = 0
        for i in str(num):
            count += 1
        if count == 6:
            break
        else:
            print ("Try again!")

    # digit1 = num // 100_000
    # digit2 = num // 10_000 % 10
    # digit3 = num // 1_000 % 10
    # digit4 = num // 100 % 10
    # digit5 = num // 10 % 10
    # digit6 = num % 10

    sum1 = 0
    sum2 = 0

    while count > 3: 
        sum1 += num % 10
        num //= 10
        count -= 1
    while count > 0:
        sum2 += num % 10
        num //= 10
        count -= 1

    if sum1 == sum2:
        print("It's a lucky ticket!")
    else:
        print("It's an unlucky ticket! ")

except:
    print("Wrong ticket number!")