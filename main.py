# Day 2 of 100 Days of Coding - The Complete Python Pro Bootcamp for 2021

# print("Hello"[0:4])
# print("Hello"[-1])

# print(len("4837"))
# print(len(str((4837))))

# two_digit_number = input("Type a two digit number:\n")
# result = ((int(two_digit_number[0])) + (int(two_digit_number[1])))
# print(two_digit_number[0])
# print(two_digit_number[1])
# print(result)

#BMI calculator
# height = float(input("Enter your height in m:\n"))
# weight = float(input("Enter your weight in kg:\n"))
# height_squared = height ** 2
# bmi = (float(weight) / (float(height_squared)))
# print("Your bmi is: " + (str(bmi)))

# f-String - allows you to concatenate different data types
# score = 95
# grade = "A"
# isPassing = True
# print(f"Your score is {score}, earning you a grade of {grade} and passing this course is {isPassing}")

# age = input("Please enter your age in days\n")
# age_years = (int(age) / 365.25)
# age_weeks = age_years * 52.0725
# age_months = age_years * 12
# ninety_days = 90 * 365.25
# ninety_weeks = 90 * 52.0725
# ninety_months = 90 * 12
# ninety_years = 90
# result_days = ninety_days - (int(age))
# result_weeks = round(ninety_weeks - (int(age_weeks)), 2)
# result_months = ninety_months - (int(age_months))
# result_years = ninety_years - (int(age_years))
# print(f"You have {result_years} years, {result_months} months, {result_weeks} weeks, and {result_days} "
#       f"days until you turn 90 years old")`

# Tip Calculator
print("Welcome to my tip calculator.")
bill = input("What was the total bill? $")
tip = input("What percentage tip would you like to give? 10, 12, etc?\n")
tip_percent = (int(tip) / 100)
payers = input("How many people to split the bill?\n")
total_bill = float(bill) + (float(bill) * tip_percent)
split = round(total_bill / int(payers), 2)
print(f"Each person should pay: ${split}")



