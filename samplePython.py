file=open("mbox-short.txt")
dictionary=dict()
for line in file:
    if line.startswith('From '):
        words=line.split()
        if words[2] not in dictionary:
            dictionary[words[2]]=[]
            dictionary[words[2]].append(words[1])
        else:
            dictionary[words[2]].append(words[1])
for day in dictionary:
    totalcount=0
    uniquecount=dict()
    for email in dictionary[day]:
            totalcount+=1
            uniquecount[email]=uniquecount.get(email,0)+1
    print("Day {} has: {} total emails registered and {} unique ones:".format(day,totalcount,len(uniquecount)))
    print(uniquecount,'\n')
    max=None
    for email in uniquecount:
        if max==None or uniquecount[email]>max:
            max=uniquecount[email]
            maxemail=email
    print("The email that can be found the most is the {} ({} times)\n".format(maxemail,max))
