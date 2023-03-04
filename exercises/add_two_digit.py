""" Get a two-digit number input from user and add that two digit."""

two_digit_number = input("Enter a two digit number: ")

# because input function always gets string. Strings can be accessed using index number
first_digit = int(two_digit_number[0]) # convert then into integer
second_digit = int(two_digit_number[1])
sum_of_digits = first_digit + second_digit
print(sum_of_digits)
