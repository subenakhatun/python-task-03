'''
Write a Python program to count the number of even and odd numbers from a series of numbers.
Sample numbers : numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
Expected Output :
Number of even numbers : 4
Number of odd numbers : 5
'''

numbers  = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even = 0
odd = 0
for num in numbers:
    if num % 2 == 0:
        even += 1
    elif num % 2 == 1:
        odd += 1
print('Number of even numbers :',even)
print('Number of odd numbers :',odd)