# Задача 2:
# Найдите сумму цифр трехзначного числа.

number = None
array = []
sum = 0

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

except:
    print("I said number!!!")
