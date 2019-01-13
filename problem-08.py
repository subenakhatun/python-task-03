'''
Write a function that returns the elements on odd positions in a list.
'''

list = [1,20,30,40,50,50,60,10,100,30,11,99,53]
empty_list = []
x = 0
for i in range(len(list)):
    if (i%2 !=0) in list:
        empty_list.append(i)
        x = x + 1
print(empty_list)

# using function
# def list():
#     empty_list = []
#     x = 0
#     for i in range(len(list)):
#         if i % 2 == 1:
#             empty_list.append(i)
#             x = x + 1
#     return empty_list
# print(list([10,80,60,33,78]))

