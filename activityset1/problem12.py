#12. Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour.

''''line = list()
hour = dict()
fname = open('activityset1/mbox-short2.txt')
for line in fname:
  if not line.startswith('From'):
    continue
  else:
    line = line.split()
    line = line[5]
    line = line.split(':')
    line = line[1]
    print(line)

for l in line:
  hour[l] = hour.get(l,0) +1

for key,value in hour.items():
  print(key,"=",value)  '''


l=list()
count = dict()
#fname = input("Enter file:")
fhandle = open('activityset1/mbox-short2.txt')

for line in fhandle:
  if line.startswith("From "):
    line=line.split()
    line=line[5]
    line=line.split(":")
    line=line[1]
    l.append(line)
    l.sort()
        
for i in l:
  count[i] = count.get(i,0) + 1
  #print(count)
  
    
for k,v in count.items():
  print(k,v)
  
    