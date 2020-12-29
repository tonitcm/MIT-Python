#Problem Set 1

#Part A

portion_down_payment = 0.25
current_savings = 0
r = 0.04 #investments earn a return of 4%
annual_salary = int(input("Enter your starting annual salary:")) #120000
portion_saved = float(input("Enter the percent of your salary to save in decimal:")) #0.10
total_cost = int(input("Enter cost of your dream home:"))#1000000
months = 0
n = 0


def house_hunting():
    print(portion_saved)
    print(total_cost)
    print(annual_salary)
down_payment = total_cost * 0.25
while current_savings <= down_payment:
    current_savings += (portion_saved*annual_salary/12) + ((current_savings * r/12))
    months = months + 1

print("Number of months: " + str(months))







#invest = current_savings * r/12

"""
Enter your annual salary: 120000
Enter the percent of your salary to save, as a decimal: .10
Enter the cost of your dream home: 1000000
Number of months: 183 
"""

