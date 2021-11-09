import random
numbertoguss = random.randint(1,20)
userguss = input("enter the number \n")
f = 0
#print(numbertoguss)
while (f==0):
   if numbertoguss != int(userguss) :
      if numbertoguss > int(userguss):
         print("smaller \n")
         userguss = input("enter the number \n")
      elif numbertoguss < int(userguss) :
         print("Larger \n")
         userguss = input("enter the number \n")
   elif numbertoguss == int(userguss) :
       print("you are win")
       f=1

