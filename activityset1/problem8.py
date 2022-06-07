#8. Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
#X-DSPAM-Confidence: 0.8475
#Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution. You can download the sample data at http://www.py4e.com/code3/mbox-short.txt.
#When you are testing below enter mbox-short.txt as the file name.


''''count = 0
total = 0
l = list()
f = open('activityset1/mbox-short2.txt')

for i in f:
  if i.startswith("X-DSPAM-Confidence"):
    w = i.split(':')
    w = float(w[-1])
    count = count+1
    l.append(w)
print(sum(l)/len(l))'''

count = 0
total = 0
l = list()
with open('activityset1/mbox-short2.txt') as f:
  l=[float(i.split(":")[-1]) for i in f if  i.startswith("X-DSPAM-Confidence")]
  print(sum(l)/len(l))





