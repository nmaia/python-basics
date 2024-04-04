try:
    hours = float(input("Enter hours: "))
    rate = float(input("Enter rate: "))
except:
    print("Error, please enter numeric input")
    quit()

if hours > 40:
    regular_pay = hours * rate
    overtime_pay = (hours - 40.0) * (rate * 0.5)
    pay = regular_pay + overtime_pay
else:
    pay = hours * rate

print("Pay:", pay)
