l=[]
for i in range (1,4):
    b=input("Enter the subject")
    l. append(b)
a="mathematics"
e="science"
c="social science"
if a in l :
    print("First priority-mathematics")
elif e in l:
    print("First priority-science")
elif c in l:
    print("First priority-social science")
else:
    print("Please select:",a,e,c)
#ENERGY LEVEL
print("Enter energy level from 1 to 3","\n","1-high","\n","2-mid","\n","3-low")
f=int(input("Enter you energy level"))
if (f==1):
      print("You are on prime!Just go with it")
elif (f==2):
      print("Not a big deal,just have reflection")
elif (f==3):
      print("Not all days are same,just get rejuvenated")
else:
    print("Sorry!Wrong choice")
#HOW'S THE PLAN
j=int(input("Enter 1 for homework or upcoming examination else enter 2"))
if (j==1) :
      print("Go with that,it's priority")
elif (j==2):
    print("Follow the above suggestions")
      
