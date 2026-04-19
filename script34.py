import csv
import os

filename = "primes.csv"


def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def get_last_prime():
    if not os.path.exists(filename):
        return 1

    with open(filename, "r", newline="") as file:
        reader = csv.reader(file)
        numbers = list(reader)

        if len(numbers) == 0:
            return 1

        return int(numbers[-1][0])


def generate_next_1000_primes(start):
    prime_list = []
    num = start + 1

    while len(prime_list) < 1000:
        if is_prime(num):
            prime_list.append([num])
        num = num + 1

    return prime_list


last_prime = get_last_prime()
new_primes = generate_next_1000_primes(last_prime)

with open(filename, "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(new_primes)

print("1000 prime numbers have been added to", filename)