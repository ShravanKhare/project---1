import random
'''

1 for snake 
0 for gun
-1 for water

'''
computer = random.choice([1,-1,0])
yourstr = input("Enter your choice: ")
yourdict = { "s":1 ,"w":-1 ,"g":0}
reversedict = {1:"snake", -1:"water" ,0:"gun"}

you = yourdict[yourstr]
    
print(f"You choose {reversedict[you]}\n Computer chose {reversedict[computer]}")

if(computer == you):
    print("Its a draw ")
else:
    if(computer==-1 and you==1):
        print("You win!! ")
    elif(computer==-1 and you==0):
        print("You loose!! ") 
    elif(computer==1 and you==0):
        print("You win!!")
    elif(computer==1 and you==-1):
        print("You loose!! ")
    elif(computer==0 and you==1):
        print("You loose!!")                   
    elif(computer==0 and you==-1):
        print("You win!! ")
    else:
        print("Something went wrong!!")    

