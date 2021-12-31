Class_List = []

lenght_List = int(input('Enter the list number: '))

for i in range(lenght_List): 
    number = float(input('enter number: '))
    
    #Class_List.append(number * number)

    Class_List.append(number)
    Class_List.remove(number)

    pow_number = number * number
    Class_List.append(pow_number)

print('\n',Class_List)
