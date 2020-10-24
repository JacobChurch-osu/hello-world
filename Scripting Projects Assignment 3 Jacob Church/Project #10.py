Hours = float(input("Enter the amount of weekly hours: "))
Overtime = float(input("Enter the amount of overtime hours: "))
HourlyWage = 10
OvertimeWage = HourlyWage * 1.5
RegPay = Hours * HourlyWage
OvertimePay = Overtime * OvertimeWage
TotalPay = RegPay + OvertimePay
print("Your total pay for the week is, $",TotalPay)

        
