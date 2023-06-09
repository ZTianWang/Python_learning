def computePay(hours, rate):
    print('Compute pay: ', hours, rate)
    if hours <= 40:
        return hours * rate
    elif hours <= 60:
        print("Overtime within 20 hours!")
        return (hours - 40) * (rate * 1.5) + 40 * rate
    else:
        print("Overtime more than 20 hours!")
        return 40 * rate + 20 * (rate * 1.5) + (hours - 60) * (rate * 2)


hoursInput = input("Hours: ")
rateInput = input("Rate: ")

try:
    hours = float(hoursInput)
    rate = float(rateInput)
except:
    input("Error: Data must be numbers!")
    quit()

pay = computePay(hours, rate)
print("Final pay: $", pay)
