import random #it's module in python which helps the computer choose a random value
"""
let:-   1 for snake
       -1 for water
        0 for gun

"""
# random.choice(sequence) fun.  use
computer=random.choice([-1,0,1])
print('ur choices:\n1)"s"\n2)"w"\n3)"g"\n')
youstr = input("Enter ur choice:") #string me
#use dictionary coz we have to use key:value
youDict={
  "s":1,"w":-1,"g":0
 }
reverse_youDict ={
1:"snake",
-1:"water",
0:"gun"

} #this converts no. back into names so,that user can understand easily
you=youDict[youstr] #convert user's choice into no.


print(f"you chose {reverse_youDict[you]}\ncomputer chose {reverse_youDict[computer]}")
#  or print(f"you chose {youDict[youstr]}\ncomputer chose {computer}")

if(computer == you):
  print("it's a draw")
else:
 
          # method 1:-
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
#method 2:-
 if((computer-you)==-1 or (computer-you)==2):
 #method 2 ka logic method 1 ko gaur se dekkhne se pta chl rha, usme jb (computer-you) kr rhe lose me serf -1 ya 2 hi aa rha
   print("you lose!!")
 else:
   print("you win!!")
   """