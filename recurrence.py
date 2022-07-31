import numpy as np
def sum(array):
    sum=0
    for i in range(len(array)):
        sum+=array[i]
    return sum

def f(k):
    R1=[8/21]
    R2=[4/21]
    R3=[2/21]
    for i in range(k):
        R2.append(R2[-1]+1)
        R3.append(R3[-1]+2/3)
        d=R2[-1]*R3[-1]*(1/3)/(R2[-1]+R3[-1]+1/3)
        R1.append(3*d)
        R3.append(d/R2[-1])
        R2.append(d/R3[-2])
    return (((R3[-1]+4/3)*(R2[-1]+1)/(R2[-1]+1+R3[-1]+4/3))+sum(R1)+1/3)/k

for i in range(1000000, 1000000+1):
    print(f(i))


