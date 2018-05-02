print('fcfs')

processes=['p1','p2','p3']
bursttime=[5,10,15]
arrivaltime=[0,1,2]
finishtime=0
starttime=0
turnaround=[0]*3
waitingtime=[0]*3
for index in range(3):
     print processes[index]
     finishtime=finishtime+bursttime[index]
     waitingtime[index]=starttime-arrivaltime[index]
     print("waiting time: "), waitingtime[index]
     turnaround[index]=finishtime-arrivaltime[index]
     print("turnaround :"), turnaround[index]
     starttime=starttime+bursttime[index]
print('number of processes: '),len(processes)  
totalwt=0 
i=0
for i in range(3):
     totalwt=totalwt+waitingtime[i]    

print ("avgtime "),totalwt/len(processes)

