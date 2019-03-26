total = 0
count = 0
a  = input('Enter a number: ')
while a == 'done':
    print(total,count,total/count)
    try:
        a = float(a)
    except:
        print('Invalid input')
        continue
    total = total + a
    count = count + 1
