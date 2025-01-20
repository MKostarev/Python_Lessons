def square_digits(num):
  result = []
  while num > 0:
    result.append((num % 10)**2)

    num //= 10

  result.reverse()
  print(result)