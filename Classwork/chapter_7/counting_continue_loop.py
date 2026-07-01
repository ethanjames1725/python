"""
Counts from 1 to 10, printing only the odd numbers.
The while loop continues until the current number is 10, and the continue
statement skips the even numbers.
"""
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)
