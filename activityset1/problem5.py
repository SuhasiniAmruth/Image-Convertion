#5. Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours. Put the logic to do the computation of pay in a function called computepay() and use the function to do the computation. The function should return a value. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).Do not worry about error checking the user input unless you want to - you can assume the user types numbers properly.


hour = float(input("Enter hours:"))
rate = float(input("Enter the rate per hour:"))
def computepay(hour,rate):
  if hour <= 40:
    return hour * rate
  else:
    return ((hour-40)*rate*1.5)+(40*rate)

print(computepay(hour,rate))