"""
Author: Janay Harris
This script reads integers from standard input, calculates sum of squares of positive numbers.
Steps:
1. Read number of test cases from first line
2. For each test case:
  - Read count of integers 
  - Read space-separated integers
  - Calculate sum of squares for positive values
3. Print results for all test cases

Rules
No for or while loops 
No list / set/ dictionary comprehension
No recursion

## Sample Input
 2
 4
 3 -1 1 14
 5
 9 6 -53 32 16

##Sample Output
206
1397
"""
import sys
import itertools

def validate_n(n):
    if not (1 <= n <= 100):
        sys.stderr.write("N must be between 1 and 100\n")
        raise SystemExit(1)
    return n

def validate_x(x):
    if not (0 < x <= 100):
        sys.stderr.write("X must be between 1 and 100\n")
        raise SystemExit(1)
    return x

def validate_y(y):
    if not (-100 <= y <= 100):
        sys.stderr.write("Each integer must be between -100 and 100\n")
        raise SystemExit(1)
    return y

def process_values(values):
    # Validate all values, then process them
    validated = map(validate_y, values)
    return sum(map(lambda x: x * x, filter(lambda x: x > 0, validated)))

def get_numbers():
    # Convert input string to integers right away
    return map(int, sys.stdin.readline().split())

def handle_case():
    count = validate_x(int(sys.stdin.readline()))
    values = get_numbers()
    # Process values will handle validation
    return process_values(values)

def process_all_cases(count):
    # Use itertools.repeat to create an iterator of None values
    # More memory effcient than intermediate string
    return map(lambda _: handle_case(), itertools.repeat(None, count))

def main():
    try:
        num_cases = validate_n(int(sys.stdin.readline()))
        results = process_all_cases(num_cases)
        sys.stdout.write('\n'.join(map(str, results)) + '\n')
    except ValueError:
        sys.stderr.write("Error: Invalid integer input\n")
        raise SystemExit(1)
    except Exception as e:
        sys.stderr.write(f"Unexpected error: {e}\n")
        raise SystemExit(1)

if __name__ == "__main__":
    main()