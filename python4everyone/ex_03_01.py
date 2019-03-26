hrs = input("Enter Hours: ")
rate = input("Enter Rate: ")
if float(hrs) >= 40:
    pay = ((float(hrs)-40)*1.5 + 40)*float(rate)
else:
    pay = float(hrs)*float(rate)
print("Pay:",pay)
