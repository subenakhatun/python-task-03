'''
Write a function that computes the running total of a list.
'''
number = int(input('Enter a running number range: '))
def sum(number):
    sum = 0
    for i in number:
        sum = sum + i
    print(sum)

sum(range(number))