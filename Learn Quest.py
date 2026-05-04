a=("Enter 1 if you want to choose among subjects")
b=("Enter 2 if you wish to know your task in a particular subject")
print(a)
print(b)
c=int(input("Enter your choice"))
if c==1:
    print("Choices are:")
    print("1:mathematics,chemistry,physics")
    print("2:social science,mathematics,english")
    print("3:physics,chemistry,biology")
    grp=int(input("Enter the group number"))
    e=int(input("Enter energy level from 1 to 3"))
    f=int(input("Enter 1 if any homework is there or exams are upcoming else enter 2"))
    g=['mathematics','chemistry','physics']
    h=['social science','mathematics','english']
    l=['physics','chemistry','biology']
    if f==1:
        print ("Prepare for exams or complete homework")
    elif f==2:
        if (grp==1)and(e==2):
            print("Choose Chemistry")
        elif (grp==1)and (e==2):
            print ("Choose Physics")
        elif (grp==1) and (e==3):
            print("ChooseMathematics")
        elif (grp==2) and (e==1):
            print("Choose English")
        elif (grp==2) and (e==2):
            print("Choose social science")
        elif (grp==2) and (e==3):
            print("Choose Mathematics")
        elif (grp==3) and(e==1):
            print("Choose chemistry")
        elif (grp==3) and(e==2):
            print("Choose biology")
        elif (grp==3) and (e==3):
            print ("Choose Physics")
        else:
             ("Kindly enter",g,h,l)
elif c==2:
    print("Enter 1 if your preparation is complete")
    print("Enter 2 if your preparation is in mid-way or feeling underconfident")
    print("Enter 3 if preparation is at its least level")
    s=int(input("Enter your choice"))
    if s==1:
        print("Go with practice")
    elif s==2:
        print("Go with Revision+10 questions practice")
    elif s==3:
        print("Focus on understanding concepts and Theory")
    else:
        print("You can refer resources like youtube")
               
    

    
      

      
      
      
