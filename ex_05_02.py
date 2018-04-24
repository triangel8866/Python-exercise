total = 0
count = 0
max = None
min = None
while True:
    a = input('Enter a number: ')
    if a == 'done':
        print(total,count,max,min)
        quit()
    try:
        a = float(a)
    except:
        print('Invalid input')
        continue
    if max == None:
        max = a
    else:
        if a > max:
            max = a
    if min == None:
        min = a
    else:
        if a < min:
            min = a
    total = total + a
    count = count + 1
