#3. Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above hours. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).Do not worry about error checking the user input - assume the user types numbers properly.

hour = float(input("Enter the hour:"))
rate = float(input("Enter the rate per hour:"))
if hour <= 40:
  gross_pay = hour * rate
  print(gross_pay)
else:
  gross_pay = ((hour-40) *rate * 1.5) + ((40)*rate)
  print(gross_pay)
  