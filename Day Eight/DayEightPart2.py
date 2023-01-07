def getTreeList(x):
    allTreeList=[]
    x=x.rstrip()
    #Puts the line into a list
    for y in x:
        allTreeList.append(y)
    #Adds zero to the start and end to represent the edge trees being visibible.
    return allTreeList

def interateTreeList(inputlist):
    y=-1
    intList=[]
    for x in range(0,(len(inputlist)-1)):
        z=inputlist[x]
        if int(z) > int(y):
            intList.append(x)
            y=z
    return intList

def getVisList(x):
    allTreeList=getTreeList(x)
    visTreeList=interateTreeList(allTreeList)
    allTreeList.reverse()
    tempTreeList=interateTreeList(allTreeList)
    for y in range(len(tempTreeList)):
        tempTreeList[y]=len(allTreeList)-tempTreeList[y]-1
    visTreeList=visTreeList+tempTreeList
    visTreeList=[*set(visTreeList)]
    return visTreeList

def horizontalToVertical(x):
    for y in range(len(x)):
        verticalTreeList.append[x]

def horizontal2Vertical(horoData):
    verticalTreeList=[]
    with open(horoData) as list:
        for x in range(len(list.readlines())):
            verticalTreeList.append([])

    with open(horoData) as list:
        count=0
        for y in list:
            y=y.rstrip()
            for z in range(len(y)):
                verticalTreeList[z].append(y[z])
    textstring='' 
    for x in verticalTreeList:
        if textstring != '':
                textstring=textstring+'\n'
        for y in x:
            textstring=textstring+y
    return textstring

file="input.txt"
verticalinput=horizontal2Vertical(file)
#List of coordinates of visable trees.
visiableTreeList=[]
#Adds the Horizontal Trees that can be seen and creates the Vertical 
with open(file) as list:
    count=0
    for x in list:
        x=x.strip()
        for w in getVisList(x):
            visiableTreeList.append(str(count)+','+str(w))
        count=count+1

count=0
for q in verticalinput.split('\n'):
    q=q.rstrip()
    if q != '':
        for p in getVisList(q):
            visiableTreeList.append(str(p)+','+str(count))
        count=count+1

visiableTreeList=[*set(visiableTreeList)]
print(len(visiableTreeList))
