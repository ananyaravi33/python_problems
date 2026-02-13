def partySuccessCheck(day, attendees):
    days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

    # Input Constraint
    if day not in days or attendees < 0:
        return "Invalid Input"

    # Weekend condition
    if day in ["FRI", "SAT", "SUN"]:
        if attendees >= 1500:
            return "Successful"
        else:
            return "Unsuccessful"

    # Weekday condition
    else:
        if 700 <= attendees <= 1000:
            return "Successful"
        else:
            return "Unsuccessful"


# Taking input
day = input("Enter the day: ").strip().upper()
attendees = int(input("Enter the attendees: ").strip())

# Calling function
result = partySuccessCheck(day, attendees)
print(result)
