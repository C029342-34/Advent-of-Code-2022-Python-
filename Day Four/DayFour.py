#Calorie count
import re
list=open("input.txt")
score=0
for x in list:
    x=re.split('-|,',x.rstrip())
    for i in range(4):
        x[i]=int(x[i])
    list1=[]
    list2=[]
    for i in range(x[1]-x[0]+1):
        i=i+x[0]
        list1.append(i)
    for i in range(x[3]-x[2]+1):
        i=i+x[2]
        list2.append(i)
    hitcount=0
    for x in list2:
        if x in list1:
            hitcount=hitcount+1
            score=score+1
            break
    if hitcount == 0 :
        hitcount=0
        for x in list1:
            if x in list2:
                hitcount=hitcount+1
                score=score+1
                break
    else :continue
print(score)
    
# for i in range(82-24):
#     print(i+24+1)
