portion_down_payment = 0.25
current_savings = 0
r = 0.04 #investments earn a return of 4%
annual_salary = int(input("Enter your starting annual salary:")) #120000
portion_saved = float(input("Enter the percent of your salary to save in decimal:")) #0.05
total_cost = int(input("Enter cost of your dream home:"))#500000
semi_annual_raise = float(input("Raise in decimal:")) #0.03
months = 0
n = 0


def house_hunting():
    print(portion_saved)
    print(total_cost)
    print(annual_salary)
    print(semi_annual_raise)
down_payment = total_cost * 0.25
while current_savings < down_payment:
        current_savings += (portion_saved*annual_salary/12) + ((current_savings * r/12)) + (semi_annual_raise/12)
        months = months + 1
        if months % 6 == 0:
            annual_salary += (semi_annual_raise*annual_salary)


print("Number of months: " + str(months))
