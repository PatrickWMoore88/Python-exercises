total_bill= int(input('Total bill amount? '))
service_level= input('Level of service? ')
if service_level == "good" or service_level == "Good" or service_level == "GOOD":
    good = total_bill * .15
    print(total_bill + good)
elif service_level == "fair" or service_level == "Fair" or service_level == "FAIR":
    fair = total_bill * .12
    print(total_bill + fair)
elif service_level == "bad" or service_level == "Bad" or service_level == "BAD" or service_level == "BAD!":
    bad = total_bill * .10
    print(total_bill + bad)
else: 
    print("Don't be cheap!")
