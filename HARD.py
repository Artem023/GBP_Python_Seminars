""" 
Найдите сумму цифр любого вещественного или целого числа. 
Можно использовать decimal. 
Через строку решать нельзя. 
"""

from decimal import Decimal as D

num = D('123456.789')
sum = 0
count = 0
print(num / 10000000)

while num != int(num):
    num *= 10


while num > 0:
    sum += num % 10
    num //= D('10')
    count += 1

print (int(sum))

# num1 = num
# while num1 > 1:
#     num1 /= 10
#     print (num1)


