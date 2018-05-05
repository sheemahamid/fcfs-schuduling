print('  virtual round robbin  ')
processes=["p1","p2","p3"]
btime=[5,10,15]
arrivaltime=[0,2,3]
starttime=0
quantum=3
turnaround=[0]*3
waitingtime=[0]*3
waitq=[0]*10
rbtime=[0]*3
t=0
i=0
iotime=5
iostime=2
rbtime = list(btime) 
returntime=[-1,-1,-1]
remainingtime=0
auxilary=[0]*3
remquantumtime=0
addv=0
remval=0

while(1):
   done ="true"
   for i in range (3):
     if cur>=returntime[remval]:
        remainingtime[i]=auxilary[remval]
        remval=remval+1
     if evenodd[i]==0:
         if rbtime[i] > 0:
            done = "false"

	      
	    if rbtime[i] > iostime:
               cur= cur+iostime
               rbtime[i]=rbtime[i]-iostime
	       returntime[i]=cur+iotime
               auxilary[addv]= returntime[i]
	       auxilary[addv]= rbtime[i]
               auxilary[addv]= position[i]	
               addv=addv+1
            elif:
                 remquantumtime<rbtime[i]
                   cur = cur+remquantumtime
		   rbtime[i]=rbtime[i]-remquantumtime
		   auxilary[remval]=returntime
 		   returntime[dequeue]=0
            else:
   	       cur = cur + rbtime[i]
	       waitingtime[i] = cur - btime[i]-arrivaltime[i]
               turnaround[i] = cur - arrivaltime[i]
	       rbtime[i]=0
               returntime[dequeue]=0
     else:
            if rbtime[i]>0:
              finish='false'
              if rbtime>quantum:
                 cur = cur+quantum
	         rbtime[i]=rbtime[i]-quantum
              else:
		    cur= cur+rbtime[i]
                    waitingtime[i] = cur - btime[i]-arrivaltime[i]
                    turnaround[i] = cur - arrivaltime[i]
	            rbtime[i]=0
   if done == "true":
     break
for index in range(3):
     print processes[index]
     t = t + btime[index]
     print("waiting time: "), waitingtime[index]
     turnaround[index]=btime[index]+waitingtime[index]
     print("turnaround :"), turnaround[index]
     starttime=starttime+btime[index]
avgwaittime=0
avgttime=0

for j in range(3):
     avgwaittime=avgwaittime+waitingtime[j]    
     avgttime=avgttime+turnaround[j]
print ("average waitingtime "),avgwaittime/len(processes)
print ("average turnaroundtime"),avgttime/len(processes)




