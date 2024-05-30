def is_prime(n):
    """Check if a number is a prime number."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        """If the number has any factors up to its square root"""
        if n % i == 0:
            return False
    return True


def get_user_input():
    """Get the range from the user and handle invalid input."""
    while True:
        try:
            start = int(input("Enter the start of the range: "))
            end = int(input("Enter the end of the range: "))
            if start > end:
                print("Start of the range must be less than or equal to the end.")
                continue
            return start, end
        except ValueError:
            print("Invalid input. Please enter integers for the range.")


def find_primes_in_range(start, end):
    """Find all prime numbers in the given range."""
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes


def main():
    """Main function to handle user input and display prime numbers."""
    print(
        """Welcome to the prime number finder! 
This application will help you list all the prime numbers in the range you provide."""
    )
    while True:
        start, end = get_user_input()
        primes = find_primes_in_range(start, end)
        if primes:
            print(f"Prime numbers between {start} and {end} are: {primes}")
        else:
            print(f"There are no prime numbers between {start} and {end}.")

        while True:
            repeat = input("Go again? (y/n): ")
            if repeat.lower() == "y":
                break  # Exit the inner loop and start a new iteration of the outer loop
            elif repeat.lower() == "n":
                print("Goodbye!")
                return  # Exit the entire main function
            else:
                print("Invalid input. Please enter 'y' or 'n'.")


if __name__ == "__main__":
    main()
