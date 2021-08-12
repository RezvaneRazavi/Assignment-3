
lenght = int(input('enter lenght= '))

for i in range (lenght):
    if i % 2 == 0:
        print('*' , end='')
    else:
        print('#' , end='')