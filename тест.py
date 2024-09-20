numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = []
not_primes = []

def is_prime(num):
    if num <= 1:
        return None
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


for num in numbers:
    if num == 1:
        continue

    is_prime_result = is_prime(num)
    if is_prime_result:
        primes.append(num)
    else:
        not_primes.append(num)

print("Primes:", primes)
print("Not Primes:", not_primes)