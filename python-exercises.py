total_bill = float(input("Total bill amount? $"))
service_level = input("Level of service? ")
split = int(input("Split how many ways? "))
if service_level == "good" or service_level == "Good" or service_level == "GOOD":
    good = total_bill * .2
    print(f"Tip amount: ${good}")
    total_plus_tax = total_bill + good
    print(f"Total bill: ${total_plus_tax}")
    total_per_person = round(total_plus_tax / split, 2)
    print(f"Amount per person: ${total_per_person}")
elif service_level == "fair" or service_level == "Fair" or service_level == "FAIR":
    fair = total_bill * .15
    print(f"Tip amount: ${fair}")
    total_plus_tax = total_bill + fair
    print(f"Total bill: ${total_per_person}")
elif service_level == "bad" or service_level == "Bad" or service_level == "BAD" or service_level == "BAD!":
    bad = total_bill * .10
    print(f"Tip amount: ${bad}")
    total_plus_tax = total_bill + bad
    print(f"Total bill: ${total_plus_tax}")
    total_per_person = round(total_plus_tax / split, 2)
    print(f"Amount per person: ${total_per_person}")
else: 
    print("Don't be cheap!")
