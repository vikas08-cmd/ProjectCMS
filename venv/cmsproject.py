
idlist=[]
namelist=[]
agelist=[]
moblist=[]
addrlist=[]
def addcustomer(id,name,age,mob,addr):
    idlist.append(id)
    namelist.append(name)
    agelist.append(age)
    moblist.append(mob)
    addrlist.append(addr)

def searchcustomer(id):
    i=idlist.index(id)
    return i

def deletecustomer(id):
    i = idlist.index(id)
    idlist.pop(i)
    namelist.pop(i)
    agelist.pop(i)
    moblist.pop(i)
    addrlist.pop(i)
def modifycustomer(id,age,name,mob,addr):
    idlist[i]=id
    namelist[i]=name
    agelist[i]=age
    moblist[i]=mob
    addrlist[i]=addr
def getid():

    if id not in idlist:
        return id
    else:
        print("duplicate id")


def getMob():
    while(1):
        mob=input("enter a mobile number")
        if(mob.isdecimal()):
            if(len(mob)==10):
              return mob
            else:
                print("enter 10 digit mobile number")
        else:
            print("enter a valid number")

   #pl
def showcustomer(index):
    print(f" name:{namelist[index]} \t age:{agelist[index]}  mobile:{moblist[index]} \t  address{addrlist[index]}")

print("welcome to Cafeteria CMS")
while(1):
     print(" 1. Add customers  2. Search customers 3. Delete customers  ")
     print("4. modify customers 5.Display all customers 6. exit")
     Choice=input("Enter your choice from above :")

     if(Choice=="1"):
        name=input("enter your name")
        while(1):
           age=input("enter your age :")
           if(12<=int(age)<=80):
               break
           else:
               print("age required above 12")
        addr=input("enter your permanent address :")
        mob=getMob()
        id=getid()
        i = name[0:6:2]+mob[0:3:2]+addr[0:12:4].upper()+mob[6:10:3]
        print(i)
        addcustomer(id,name,age,mob,addr)
        print("customer addedd sucessfully :")
     elif(Choice=="2"):
        id=input("enter id to search customer :")
        index=searchcustomer(id)
        showcustomer(index)

        print("search result ends")
     elif(Choice=="3"):
        id=input("enter id to delete customers")
        deletecustomer(id)
        print("customer deleted sucessfully")
     elif(Choice=="4"):
        id=input("enter id to modify customer")
        name=input("enter customer name to update")
        age=input("enter customer age to update")
        mob=input("enter customwr mobile to update")
        addr=input("enter customer address to update")
        modifycustomer(id,name,age,mob,addr)
        print("customer modified sucessfully")
     elif(Choice=="5"):
         for i in range(len(idlist)):
             showcustomer(i)

     elif(Choice=="6"):
        print("thanks for using cafeteria  CMS")
        break
     else:
        print("incorrect choice please enter again")






