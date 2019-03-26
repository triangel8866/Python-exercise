hrs = input("Enter Hours: ")
try:
    hr = float(hrs)
except:
    print("Error, please enter numeric input")
    quit()

rate = input("Enter Rate: ")
try:
    rt = float(rate)
except:
    print("Error, please enter numeric input")
    quit()

if float(hrs) >= 40:
    pay = ((hr-40)*1.5 + 40)*rt
else:
    pay = hr*rt
print("Pay:",pay)
