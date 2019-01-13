'''
Implement binary search.
'''
list = [20,21,22,30,40,45,48,50,60,70,80,90]
search_number = 50
first_index = 0
last_index = len(list)-1
# print(last_index)
find = False
while first_index <= last_index and not find:
    mid = int((last_index + first_index)/2)
    if list[mid] == search_number:
        find = search_number
    else:
        if search_number < list[mid]:
            last_index = mid - 1
        else:
            first_index = mid + 1
print('find the number: ',find)