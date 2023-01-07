#Calorie count
list=open("input.txt")
score=0
for x in list:
    x=x.rstrip().split()
    if x[0] == 'A': # Rock 1 
        if x[1] == 'X': # Lose
            score=score+0+3
        elif x[1] == 'Y': # Draw
            score=score+3+1
        elif x[1] == 'Z': # Win
            score=score+6+2
        else:continue
    elif x[0] == 'B': # Paper  2
        if x[1] == 'X': # Lose
            score=score+0+1
        elif x[1] == 'Y': # Draw
            score=score+3+2
        elif x[1] == 'Z': # Win
            score=score+6+3
        else:continue
    elif x[0] == 'C': # Scissors 3  
        if x[1] == 'X': # Lose
            score=score+0+2
        elif x[1] == 'Y': # Draw
            score=score+3+3
        elif x[1] == 'Z': # Win
            score=score+6+1
        else:continue
    else: continue
print(score)    




