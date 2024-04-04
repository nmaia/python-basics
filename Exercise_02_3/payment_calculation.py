try:
    hours = float(input("Enter hours: "))
    rate = float(input("Enter rate: "))
except:
    print("Error, please enter numeric input")
    quit()

def computepay(hours, rate):
    if hours > 40:
        regular_pay = hours * rate
        overtime_pay = (hours - 40.0) * (rate * 0.5)
        pay = regular_pay + overtime_pay        
    else:
        pay = hours * rate    
    return pay

pay = computepay(hours, rate)

print("Pay:", pay)
