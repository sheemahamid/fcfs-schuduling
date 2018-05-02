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
print rbtime
