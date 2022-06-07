#11. Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

person=list()
count=dict()
fname = open('activityset1/mbox-short2.txt')
for line in fname:
  if line.startswith('From'):
    words = line.split()
    person.append(words[2])
    #print(words)
#print(person)

for p in person:
  count[p] = count.get(p,0)+1
print(count)
print("\n")

for a,b in count.items():
  print(a, "appeared", b, "times in the file")
  


