#Calorie count
list=open("input.txt")
score=0
wrongitems=[]
count=0
interitems=[]
for x in list:
    x=x.rstrip()
    if count == 0:
        elfone=x
        count=count+1
    elif count == 1:
        elftwo=x
        count=count+1
    else: 
        elfthree=x
        for letters in elfone:
            if elftwo.find(letters) != -1 :
                interitems.append(letters)
        for letterstwo in interitems:
            if elfthree.find(letterstwo) != -1:
                wrongitems.append(letterstwo)
                break
        count=0
        interitems=[]

print(wrongitems)
count=0
valuedict={}
valuelist=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
for letters in valuelist:
    count=count+1
    valuedict[letters]=count
for y in wrongitems:
    score = score + valuedict[y]

print(score)


