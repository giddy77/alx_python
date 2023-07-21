
def main():
    is_prime(17)
    is_prime(15)
    is_prime(-5)
    is_prime(0)


def is_prime(number):
    if number <= 1:
        return False

    for divisor in range(2, int(number**0.5) + 1):
        if number % divisor == 0:
            return False

    return True

main()