print('sjf')
print('number of processes')
processes=['p1','p2','p3']
bursttime=[5,10,15]
arrivaltime=[0,0,0]
finishtime=0
starttime=0
turnaround=[0]*5
waitingtime=[0]*5
minimum=bursttime[0]
index=0
i=0
j=0
for i in range(2):
    for j in range(2-i):
	if bursttime[j]>bursttime[j+1]: 
             temp=bursttime[j]
             bursttime[j]=bursttime[j+1]
             bursttime[j+1]=temp
	     temp1=processes[j]
             processes[j]=processes[j+1]
             processes[j+1]=temp

for index in range(3):
    print processes[index]
    finishtime=finishtime+bursttime[index]
    waitingtime[index]=starttime-arrivaltime[index]
    print waitingtime[index]
    turnaround[index]=finishtime-arrivaltime[index]
    print turnaround[index]
    starttime=starttime+bursttime[index]
     
