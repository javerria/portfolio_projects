# Prime Number Finder

## Description
This application helps you find all the prime numbers within a specified range. Users can input two numbers representing the start and end of the range, and the application will output all the prime numbers within that range. The application includes error handling for invalid inputs and allows users to continue searching for prime numbers in different ranges.

## How to Run the Application
1. Ensure you have Python installed on your machine.
2. Save the script (`01_time_complexities.py`) to your local directory.
3. Open a terminal and navigate to the directory containing `01_time_complexities.py`.
4. Run the script using the command:
   ```
   python 01_time_complexities.py
   ```


## Explanation of Time Complexities
### is_prime(n)

The ```is_prime``` function checks if a number $n$ is prime by iterating from $2$ to the square root of $n$.

Time Complexity: 
$\( O(\sqrt{n}) \)$

​
The function performs approximately $\sqrt{n}$ checks to determine if $n$ is divisible by any number in this range.

### get_user_input()

The ```get_user_input``` function prompts the user for input and ensures the input is valid.

Time Complexity: $\(O(1)\)$

The function operates in constant time, as it only involves a fixed number of operations regardless of the input size.

### find_primes_in_range(start, end)

The ```find_primes_in_range``` function finds all prime numbers in the specified range by calling ```is_prime``` on each number in the range.

Time Complexity: $\( O((\text{end} - \text{start} + 1) \cdot \sqrt{m}) \)$

The function iterates over $\((\text{end} - \text{start} + 1)\)$ numbers.
For each number num, it calls ```is_prime```, which takes $\( O(\sqrt{num}) \)$ time.
Assuming num varies linearly, $\(m\)$ represents the average value in the range, so the complexity is $\( O(\sqrt{m}) \)$ per number.

### main()
The ```main``` function handles user interaction, calling ```get_user_input``` and ```find_primes_in_range``` as needed, and prompts the user to continue or exit.

Time Complexity: The complexity depends on user interaction:
User Input Handling: $\( O(1) \)$
Finding Primes: $\( O((\text{end} - \text{start} + 1) \cdot \sqrt{m}) \)$

Overall: $\( O(k \cdot (\text{end} - \text{start} + 1) \cdot \sqrt{m}) \)$ where $\(k\)$ is the number of times the user repeats the process.
