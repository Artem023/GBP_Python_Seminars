# Задача 2:
# Найдите сумму цифр трехзначного числа.

number = None
array = []
sum = 0
sum2 = 0

try:
    while True:
        number = int(input("Type random number: "))
        if 100 <= number <= 999:
            break
        else:
            print("Type correct number!")

    # Способ №1 
    first_digit = int(number / 100)
    second_digit = int(number / 10 % 10)
    third_digit = number % 10
    result = first_digit + second_digit + third_digit

    print(result)
    
    # Способ №2
    array = [int(i) for i in str(number)]
    for i in array:
        sum += i
    print (sum)

    # Способ №3
    while number != 0:
        sum2 += number % 10
        number //= 10
    print (sum2)

    # Способ №
except:
    print("I said number!!!")
