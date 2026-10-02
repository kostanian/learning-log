def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    replaced_dollars=float(d.replace("$",""))
    return replaced_dollars



def percent_to_float(p):
    replaced_percent=p.replace("%","")
    replaced_percent_float=float(replaced_percent)/100
    return replaced_percent_float


main()