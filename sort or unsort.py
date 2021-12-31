Array_list =  []


lenght_list = int(input('enter number of array: '))

for i in range(lenght_list):
    number = int(input('enter number: '))
    Array_list.append(number)


for i in range(lenght_list - 1):
    
    if Array_list[i] < Array_list[i + 1]:    
        continue
        
    else:
        print('Array is not Sort.')
        break
    
print('Array is Sort.')
