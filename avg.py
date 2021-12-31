counter = int (input('Enter the number of students : '))

sum = 0
score = []
max = 0
min = 20

for i in range(counter) :
    num = float ( input ('Enter score : '))

    score.append (num)

for i in range (counter) :
    sum = sum + score [i]

print ('avg =  ' , sum/counter)

for i in range (counter) :
    if score[i] > max :
        max = score[i]
    if score[i] < min :
        min = score[i]

print ('max = ' , max)
print ('min = ' , min)
