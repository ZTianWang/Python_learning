# The pay rate of the part of 40 to 60 hours is 1.5 times and upper 60 hours is 2 times than regular time

hoursInput = input("Hours: ")
rateInput = input("rate: ")

# Catch exception:
try:
    hours = float(hoursInput)
    rate = float(rateInput)
except:
    input("Error: Data must be numbers!")
    # quit(): do not continue
    quit()

# Conditional statement: (if, elif, else)
if hours <= 40:
    pay = hours * rate
elif hours <= 60:
    print("Overtime within 60 hours!")
    pay = (hours - 40) * (rate * 1.5) + 40 * rate
else:
    print("Overtime more than 60 hours!")
    pay = 40 * rate + 20 * (rate * 1.5) + (hours - 60) * (rate * 2)

print("Final pay: $", pay)
