import random
import sys

def generate_random_numbers(count):
    """Generates a list of random numbers."""
    return [random.randint(1, 100) for _ in range(count)]

def find_prime_numbers(numbers):
    """
    Finds prime numbers from a given list.
    Args:
        numbers (list): List of numbers to check for primality.
    Returns:
        list: List of prime numbers found.
    """
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
        count = int(sys.argv[1])  # Get the number of random numbers from command line argument
    except IndexError:
        print("Please provide the number of random numbers to generate.")
        return
    except ValueError:
        print("Please provide a valid integer.")
        return
    
    if count <= 0:
        print("Please provide a positive integer.")
        return
    
    random_numbers = generate_random_numbers(count)  # Generate random numbers
    
    prime_numbers = find_prime_numbers(random_numbers)  # Find prime numbers
    
    # Print results
    print("Generated Random Numbers:", random_numbers)
    print("Prime Numbers:", prime_numbers)

if __name__ == "__main__":
    main()
