et = input("Enter score:")
try:
    etf = float(et)
except:
    print("Bad score")
    quit()

if etf >= 0 and etf <= 1:
    if etf >= 0.9:
        print("A")
    elif etf >= 0.8:
        print("B")
    elif etf >= 0.7:
        print("C")
    elif etf >= 0.6:
        print("D")
    else:
        print("F")
else:
    print("Bad score")
