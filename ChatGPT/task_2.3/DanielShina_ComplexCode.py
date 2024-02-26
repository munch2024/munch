import random, sys

def generate_random_numbers(n):
    return [random.randint(1, 100) for _ in range(n)]

def filter_odd_numbers(numbers):
    return [num for num in numbers if num % 2 != 0]

def calculate_square_roots(numbers):
    return [num ** 0.5 for num in numbers]

def find_prime_numbers(numbers):
    prime_numbers = []
    for num in numbers:
        if num > 1:
            is_prime = True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                prime_numbers.append(num)
    return prime_numbers

def main():
    try:
        n = int(sys.argv[1])
    except IndexError:
        print("Please provide the number of random numbers to generate.")
        return
    except ValueError:
        print("Please provide a valid integer.")
        return

    random_numbers = generate_random_numbers(n)
    odd_numbers = filter_odd_numbers(random_numbers)
    square_roots = calculate_square_roots(odd_numbers)
    prime_numbers = find_prime_numbers(square_roots)

    print("Generated Random Numbers:", random_numbers)
    print("Filtered Odd Numbers:", odd_numbers)
    print("Square Roots:", square_roots)
    print("Prime Numbers from Square Roots:", prime_numbers)

if __name__ == "__main__":
    main()
