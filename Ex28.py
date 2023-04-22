# Напишите рекурсивную функцию sum(a, b), 
# возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. 
# Также нельзя использовать циклы.

def recur_sum(n):
       if n <= 1: 
               return n 
       else: 
               return n + recur_sum(n-1) 
num = int( ) 

if num < 0: 
       print("Enter a positive number: ") 
else: 
       print("The sum is ", recur_sum(num)) 