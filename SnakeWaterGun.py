import random #Import random module to randomly select number representing the computer's choice

"""
let:-   1 for snake
       -1 for water
        0 for gun

"""
# random.choice(sequence) fun. 
computer=random.choice([-1,0,1]) #randoly choose -1,0 or 1 for the computer

print('ur choices:\n1)"s"\n2)"w"\n3)"g"\n')   # display the available choices to the user.


youstr = input("Enter ur choice:") #take the user's choice in a string 


youDict={  #use dictionary for mapping(converting) user input to game values.....
  "s":1,"w":-1,"g":0
 }

reverse_youDict ={ #dictionary to convert numeric values back into readable names so,that user can understand easily
1:"snake",
-1:"water",
0:"gun"

}
you=youDict[youstr] #convert the user's choice into it's corresponding numeric value


print(f"you chose {reverse_youDict[you]}\ncomputer chose {reverse_youDict[computer]}") #display both the user's and the computer's choices
#  or print(f"you chose {youDict[youstr]}\ncomputer chose {computer}")

if(computer == you): #it will check if the game ends in a draw
  print("it's a draw")
else:
 
          # method 1:-Determine the winner using conditional statements
  if(computer==-1 and you==0):
    print("you lose!!")
  elif(computer==-1 and you==1):
    print("you win!!")
  elif(computer==1 and you==-1):
    print("you lose!!")
  elif(computer==1 and you==0):
    print("you win!!")
  elif(computer==0 and you==-1):
    print("you win!!")
  elif(computer==0 and you==1):
    print("you lose!!")
  else:
    print("Somthing went wrong!!")

"""
          #  method 2:-Determine the winner using Mathematical statements


  if((computer-you)==-1 or (computer-you)==2):
   
    #using mathematical logic....from conditional statement above , the difference (computer-you) is -1 or 2 when the player loses. otherwise,the player wins....

    print("you lose!!") 

  else:
    print("you win!!")
    
"""