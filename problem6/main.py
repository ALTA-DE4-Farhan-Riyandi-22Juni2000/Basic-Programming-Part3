def full_prima(N):
  def prime_number(number):
    if number <= 1:
      return False

    elif number > 1:
      # cek faktor
      for i in range(2, number):
        if number % i == 0:
          return False
          break
      else:
        return True
  # Memeriksa apakah bilangan itu sendiri adalah bilangan prima
  if not prime_number(N):
    return False

  for digit in str(N):
    if not prime_number(int(digit)):
      return False

  return True

if __name__ == '__main__':
    print(full_prima(2)) # True
    print(full_prima(3)) # True
    print(full_prima(11)) # False
    print(full_prima(13)) # False
    print(full_prima(23)) # True
    print(full_prima(29)) # False
    print(full_prima(37)) # True
    print(full_prima(41)) # False
    print(full_prima(43)) # False
    print(full_prima(53)) # True