input=open('input.txt.txt')
pwd=[]
directorydict={}
sum=0
for x in input:
    x=x.rstrip()
    if x.startswith('$'):
        x=x.lstrip('$ ')
    if x.startswith('cd'):
        directory=x.split()[1]
        if directory == '/':
            pwd=['/']
        elif directory == '..':
            pwd=pwd[:-1]
            if not pwd:
                pwd=['/']
        else:
            pwd.append(directory)
    elif x.startswith('ls'):
        continue
        # print(pwd)
        # workingdict=directorydict
        # for y in pwd:
        #     dictcheck=workingdict.get(y,0)
        #     if dictcheck == 0:
        #         workingdict[y]={}
    else:
        if x.startswith('dir'):
            continue
        elif x == '': continue
        else:
            x=x.split()
            x=int(x[0])
            for y in range(len(pwd)):
                if y == 0:
                    dictvalue=directorydict.get(y,0)
                    directorydict[str(pwd)]=dictvalue+x
                else : 
                    dictvalue=directorydict.get(y,0)
                    directorydict[str(pwd[:-y])]=dictvalue+x



            # for y in pwd:
            #     dictvalue=directorydict.get(y,0)
            #     directorydict[y]=dictvalue+x
for (k,v) in directorydict.items():
    if v <= 100000:
        sum=sum+v
print(sum)
