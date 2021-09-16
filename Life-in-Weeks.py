#Input your name, age and wish
NAME = str(input("Enter your name: "))
AGE = int(input("Enter your age: "))
wishAGE = int(input("Enter your wish to live (age): "))

#years calculate
remaining_years = (wishAGE - AGE)
#months calculate
remaining_months = (remaining_years * 12)
#weeks calculate
remaining_weeks = (remaining_years * 52)
#days calculate
remaining_days = (remaining_years * 365)

print(f"Your remaining life expectancy is {remaining_years} years or {remaining_months} months or {remaining_weeks} weeks or {remaining_days} days")