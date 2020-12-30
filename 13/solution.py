import sys
import re

arrive = int(sys.stdin.readline())
_buses = sys.stdin.readline().split(',')

buses = []
for n,bus in enumerate(_buses):
    try:
        buses.append( (n,int(bus)) )
    except:
        pass


print(arrive)
print(buses)

_,wait = buses[-1]
for _,bus in buses:
    _wait = bus-arrive%bus
    if _wait < wait:
        wait = _wait
        bus2 = bus

print(wait,bus2,wait*bus2)


eqs = list( (-n%bus,bus) for n,bus in buses )
#eqs = list( (-n,bus) for n,bus in buses )
print(eqs)

N = 1
for _,bus in buses:
    N *= bus
print(N)

chinese = 0
for a,n in eqs:
    s = pow(N//n,-1,n)
    print(a,n,s)
    chinese += a*s*N//n

print(chinese)
print(chinese%N)


time = 0
increment = buses[0][1]
for i in range(1,len(buses)):
    while (time+buses[i][0])%buses[i][1] != 0:
        time += increment
    increment *= buses[i][1]
    print(time)
