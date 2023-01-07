#Calorie count
list=open("input.txt").read()
buffer=[]
count=0
print(list)
for x in list:
    count=count+1
    if count < 14:
        buffer.append(x)
        continue
    buffer.append(x)
    deduplist = [*set(buffer)]
    if len(deduplist) < 14:
        buffer=buffer[1:]
    else:
        print(buffer,count)
        break
