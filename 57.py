def square_digits(num):
    result = []
    while num > 0:
        result.append((num % 10) ** 2)
        num //= 10
    result.reverse()
    if result == []:
        return (0)
    else:
        number = int(''.join(map(str, result)))
        return (number)


square_digits(0)