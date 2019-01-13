'''
Write a program that prints the next 20 leap years.

'''


given_number = int(input('Enter given number: '))
list = []
x = 0
while x < 20:
    if given_number % 100 == 0 or given_number % 400 == 0 and given_number % 4 == 0:
         x = x + 1
         list.append(given_number)
    given_number = given_number + 1
print('next 20 years leap year: ',list)
print('\n')
# using function

def leapyear(given_number):
    list = []
    x = 0
    while x < 20:
        if given_number % 100 == 0 or given_number % 400 == 0 and given_number % 4 == 0:
            x = x + 1
            list.append(given_number)
        given_number = given_number + 1
    return list
print('using function: ',leapyear(2019))

