#Define constant: total students=91
#Define initial variable : initial infectors=5
#Define daily growth rate: growth rate=0.4
#Initialize the day: day passed=0
#while loop: while current infector< total students ,there have
#day passed +1
#calculate new infector = current infector*(1+ growth rate)
#round up new infector
#update day passed and current infector
#print  day passed and current infector
#after loop ends, print total days passed
import math
ts=91
ci=5
gr=0.4
dp=0
while ci < ts:
    dp=dp+1
    ci=ci*(1+gr)
    ci=math.ceil(ci)
    if ci>ts:
        ci+ts
    print(f"Day{dp}, {ci} students infected")
print(f"ALL {ts} STUDENTS ARE INFECTED!")
print(f"It takes {dp} days")
