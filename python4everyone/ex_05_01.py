total = 0
count = 0
while True:
    a = input('Enter a number: ')
    if a == 'done':
        print(total,count,total/count)
        quit()
    try:
        a = float(a)
    except:
        print('Invalid input')
        continue
    total = total + a
    count = count + 1
