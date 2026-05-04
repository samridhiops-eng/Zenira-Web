a=int(input("Enter your class"))
b=input("Do you want suggestion for science or mathematics?")
if (b=="science"):
    if (a==9):
        print("S.Chand is a perfect match")
    elif (a==10):
        print ("S.Chand would be most suitable and you can also refer Physics Wallah or Together With Question Banks for practice")
    elif(a==11)or(a==12):
        print("Physics-Pradeep's,Chemistry-Pradeep's,Biology-NCERT or Trueman's for school level")
        print("FOR JEE-Pysics=H.C Verma,Chemistry=Cengage")
        print("FOR NEET-Trueman's publications and NCERT is the real bible")
elif (b=="mathematics"):
    if(a==9):
        print("R.S Aggarwal")
    elif(a==10):
        print("R.S Aggarwal and Question Banks-Together With")
    elif(a==11)or(a==12):
        print("R.D Sharma and FOR JEE-Cengage or Arihant's V.Govorov")
        
        
