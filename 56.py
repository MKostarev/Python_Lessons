#Завершите функцию, которая принимает в качестве входных данных неотрицательное целое число nи возвращает список всех степеней числа 2с показателем степени от 0до n(включительно).
#
#Примеры
#n = 0  ==> [1]        # [2^0]
#n = 1  ==> [1, 2]     # [2^0, 2^1]
#n = 2  ==> [1, 2, 4]  # [2^0, 2^1, 2^2]



def powers_of_two(n):
    list=[]
    for i in range(0,n+1):
        list.append(2**i)
    return list

powers_of_two(3)