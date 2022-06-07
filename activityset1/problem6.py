#6. Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number, catch it with a try/except and put out an appropriate message and ignore the number. 

large = -1
small = 1000
n = list()

while True:
  num = input("Enter the number:")
  try:
    number = int(num)
  except:
    if num == 'done':
      break
    else:
      print("invalid number")

  if number > large:
    large = number
  if number < small:
    small = number
    
#while True:
 # number = input("Enter the number/done to stop:")
  #try:
   # num = int(number)
    #n.append(num)
    
 # except:
  #  if number == "done" :
   #   break
    #else:
     # print("invalid input")
      
#print("Entered numbers are:",n)   
#for i in n:
 # if i > large:
  #  large = i

print("The largest number is:", large)
print("The smallest number is:",small)
    
  
 





                                                 
