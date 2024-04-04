hours = float(input("Enter hours: "))
rate = float(input("Enter rate: "))

if hours > 40:
    # print("Overtime")
    regular_pay = hours * rate
    overtime_pay = (hours - 40.0) * (rate * 0.5)
    pay = regular_pay + overtime_pay
else:
    # print("Regular")
    pay = hours * rate

print("Pay:", pay)
