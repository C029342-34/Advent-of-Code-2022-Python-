#Calorie count
list=open("input.txt")
caloriedict={}
count=0
total=0
for x in list:
    x=x.rstrip()
    if x == '':
        caloriedict[count]=total
        total=0
        count=count+1
    else : 
        total = total + int(x) 
calorielist=[]
for (k,v) in caloriedict.items():
    calorielist.append(v)
calorielist.sort()
print(calorielist)
total=0
for items in calorielist[-3:]:
    total=total+items
print(total)




