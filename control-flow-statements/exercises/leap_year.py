""" a year is a leap year if it is divisible by 4, except for years that are divisible by 100.
However, years that are divisible by 400 are still considered leap years.
"""
# Prompt the user to enter a year
year = int(input("Enter a year: "))

# Check if the year is divisible by 4
if year % 4 == 0:
    # If the year is divisible by 4, check if it is divisible by 100
    if year % 100 == 0:
        # If the year is divisible by both 4 and 100, check if it is divisible by 400
        if year % 400 == 0:
            # If the year is divisible by both 4, 100, and 400, it is a leap year
            print(f"{year} is a leap year.")
        else:
            # If the year is not divisible by 400, it is not a leap year
            print(f"{year} is not a leap year.")
    else:
        # If the year is divisible by 4 but not by 100, it is a leap year
        print(f"{year} is a leap year.")
else:
    # If the year is not divisible by 4, it is not a leap year
    print(f"{year} is not a leap year")
