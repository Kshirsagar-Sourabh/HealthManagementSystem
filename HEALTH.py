def getdate():
    import datetime
    return datetime.datetime.now()
def takeLR(c):
    if(c==1):
        fe=int(input("Press \n1.Exercise\n2.Food\n"))  # for food or exercise
        if(fe==1):
            s1=open("Sourabh-Ex.txt","a")
            w1=input("Enter the Data\n")
            s1.write(str([str(getdate())])+": "+w1+"\n")
            s1.close()
        elif(fe==2):
            s11=open("Sourabh-Food.txt","a")
            w11=input("Enter the Food you ate\n")
            s11.write(str([str(getdate())])+": "+w11+"\n")
            s11.close()
    if(c==2):
        fe=int(input("Press \n1.Exercise\n2.Food\n"))  # for food or exercise
        if(fe==1):
            s1=open("Sahil-Ex.txt","a")
            w1=input("Enter the Data\n")
            s1.write(str([str(getdate())])+": "+w1+"\n")
            s1.close()
        elif(fe==2):
            s11=open("Sahil-Food.txt","a")
            w11=input("Enter the Food you ate\n")
            s11.write(str([str(getdate())])+": "+w11+"\n")
            s11.close()
    if(c==3):
        fe=int(input("Press \n1.Exercise\n2.Food\n"))  # for food or exercise
        if(fe==1):
            s1=open("Sanket-Ex.txt","a")
            w1=input("Enter the Data\n")
            s1.write(str([str(getdate())])+": "+w1+"\n")
            s1.close()
        elif(fe==2):
            s11=open("Sanket-Food.txt","a")
            w11=input("Enter the Food you ate\n")
            s11.write(str([str(getdate())])+": "+w11+"\n")
            s11.close()

def recollect(c):
    if(c==1):
        fe=int(input("Press \n1.Exercise\n2.Food\n"))  # for food or exercise
        if(fe==1):
            s1=open("Sourabh-Ex.txt","r")
            v=s1.read()
            s1.close()
        elif(fe==2):
            s11=open("Sourabh-Food.txt","r")
            v=s11.read()
            s11.close()
    if(c==2):
        fe=int(input("Press \n1.Exercise\n2.Food\n"))  # for food or exercise
        if(fe==1):
            s1=open("Sahil-Ex.txt","r")
            v=s1.read()
            s1.close()
        elif(fe==2):
            s11=open("Sahil-Food.txt","r")
            v=s11.read()
            s11.close()
    if(c==3):
        fe=int(input("Press \n1.Exercise\n2.Food\n"))  # for food or exercise
        if(fe==1):
            s1=open("Sanket-Ex.txt","r")
            v=s1.read()
            s1.close()
        elif(fe==2):
            s11=open("Sanket-Food.txt","r")
            v=s11.read()
            s11.close()
    
    return v
         
print("HEALTH MANAGEMENT SYSTEM ")
print("Press\n1.Log\n2.Retrieve the Value ") 
t=int(input())  #taking value for log and retrieve
print("Press \n1.Sourabh\n2.For Sahil\n3.For Sanket")
c=int(input())  #for choosing the name 
if(t==1):
    takeLR(c)
elif(t==2):
    v=recollect(c)
    print(v)
else:
    print("Invalid")