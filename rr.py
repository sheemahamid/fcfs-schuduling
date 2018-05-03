print('  round robbin  ')
processes=["p1","p2","p3"]
btime=[5,10,15]
arrivaltime=[0,0,0]
finishtime=0
starttime=0
turnaround=[0]*3
waitingtime=[0]*3
timeslice = 3
rbtime=[0]*3
i=0
rbtime = list(btime) //copying the list
while(1):
   done ="true"
   for i in range (3):
       if rbtime[i] > 0:
           done = "false"
	   if rbtime[i] > quantum:
               t= t+quantum
	       rbtime[i]=rbtime[i]-quantum
	   else:
   	       t=t+rbtime[i]
	       waitingtime[i] = t - btime[i]-arrivaltime[i]
               turnaround[i] = t - arrivaltime[i]
	       rbtime[i]=0
   if done== "true":
     break
for index in range(3):
     print processes[index]
     t = t + btime[index]
     print("waiting time: "), waitingtime[index]
     turnaround[index]=btime[index]+waitingtime[index]
     print("turnaround :"), turnaround[index]
     starttime=starttime+btime[index]
