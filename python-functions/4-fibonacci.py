def main():
    fibonacci_sequence(6)
    fibonacci_sequence(1)
    fibonacci_sequence(0)
    fibonacci_sequence(20)

def fibonacci_sequence(n):
    if n <= 0:
        return []

    fibonacci_list = [0, 1]
    while len(fibonacci_list) < n:
        next_fibonacci = fibonacci_list[-1] + fibonacci_list[-2]
        fibonacci_list.append(next_fibonacci)

    return fibonacci_list
    

main()