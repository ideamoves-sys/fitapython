stock_prices = [('Appl', 200),('Goog', 400), ('Msft', 100)]

for item in stock_prices:
    print(item)

for ticker,price in stock_prices:
    print(price + (0.1*price))

//No by using the function

work_hours = [('Ash', 100), ('Kumar', 200),('AK', 800)]

def employee_check(work_hours):
    current_max = 0;
    employye_of_month = ''

    for employee,hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass
    return (employee_of_month, current_max)

employee_check(work_hours)

result = employee_check(work_hours)

#name, hours = employee_check(work_hours)
