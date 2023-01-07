#Calorie count
list=open("input.txt")
ystring=[]
#crates=[[],[],[]]
crates=[[],[],[],[],[],[],[],[],[]]
moves=[]
# Creates the list of the crates
for x in list:
    x=x.rstrip()
    if x == '':
        break
    x=x[1:]
    count=0
    y=''
    while len(x) >= count:
        y=y+x[count]
        count=count+4
    ystring.append(y)
ystring.reverse()
for x in ystring:
    if x[0] == '1':
        continue
    for i in range(len(x)):
        if x[i] != ' ':
            crates[i].append(x[i])
#Creates a list of the moves.
for x in list:
    x=x.rstrip()
    if x.startswith('move') != True:
        continue
    x=x.split()
    x=[x[1],x[3],x[5]]
    moves.append(x)
print(crates,moves)
#Iterates through the moves to change the crates
for x in moves:
    quantity=int('-'+x[0])
    source=crates[int(x[1])-1]
    destination=crates[int(x[2])-1]
    #Add crates to Destination
    items=source[quantity:]
    #items.reverse()
    for y in items:
        crates[int(x[2])-1].append(y)
    #Remove crates from Source]
    crates[int(x[1])-1]=source[:quantity]
#Answer
answer=''
for v in crates:
    try: 
        answer=answer+v[-1]
    except:continue
print(answer)