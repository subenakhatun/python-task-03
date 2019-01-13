'''
Li = [25,2,56,12,9,3,2,5,1,4,1,58,36,96,4]
Read max number algorithm from internet . and  find max number in ‘li’
Note: don’t use python built in max function

'''
li = [25,2,56,12,9,3,2,5,1,4,1,58,36,96,4]
max_value = 0
length = len(li)
for i in range(1,length):
    if li[i] > max_value:
        max_value = li[i]
print('Maximum value is: ',max_value)





