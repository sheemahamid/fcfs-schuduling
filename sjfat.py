print('sjf')
print('number of processes')
processes=['p1','p2','p3']
bursttime=[5,9,6]
arrtime=[0,3,6]
finishtime=0
starttime=0
turnaround=[0]*5
waitingtime=[0]*5
minimum=bursttime[0]
index=0
i=0
j=0
curtime=0
for i in range(2):
    for j in range(2-i):
	if bursttime[j]>bursttime[j+1] and arrtime[i]>curtime:
             temp=bursttime[j]
             bursttime[j]=bursttime[j+1]
             bursttime[j+1]=temp
	     temp1=processes[j]
             processes[j]=processes[j+1]
             processes[j+1]=temp
    curtime=curtime+bursttime[i]
for index in range(3):
    print processes[index]
    finishtime=finishtime+bursttime[index]
    waitingtime[index]=starttime-arrtime[index]
    print("waiting time:"), waitingtime[index]
    turnaround[index]=finishtime-arrtime[index]
    print("turnaround time:"), turnaround[index]
    starttime=starttime+bursttime[index]

avgwait=0
avgturn=0
for j in range(3):
     avgwait=avgwait+waitingtime[j]    
     avgturn= avgturn+turnaround[j]
print ("average waiting time "),avgwait/len(processes)
print("average turnaroundtime"),avgturn/len(processes)

