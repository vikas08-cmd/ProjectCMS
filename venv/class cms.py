class customer:
    STORAGE=[]
    def __init__(self):
        self.id=0
        self.name=0
        self.age=0
        self.mobile=0
    def addcustomer(self):
        customer.STORAGE.append(self)
    def searchcustomer(self):
        for e in customer.STORAGE:
            if(e.id == self.id):
                self.name=e.name
                self.age=e.age
                self.mobile=e.mobile
    def deletecustomer(self):
        for e in customer.STORAGE:
            if(e.id== self.id):
                customer.STORAGE.remove(e)
                return true

        return false



    def modifycustomer(self):
        for e in customer.STORAGE:
            if(e.id== self.id):
                e.name=self.name
                e.age=self.age
                e.mobile=self.mobile



print("welcome to vikas CMS")
def showcustomer(ob):
    print(f"cusid-{ob.id},name-{ob.name},age-{ob.age},mob-{ob.mobile}")
while(1):
    print("1.add customer 2.search customer 3. delete customer")
    print("4.modify customer 5.Display all customer 6.exit")
    choice=input("enter your choice -")
    if(choice=="1"):
        ob=customer()
        ob.id=input("enter your id")
        ob.name=input("enter your name")
        ob.age=input("enter your age")
        ob.mobile=input("enter your mobile number")
        ob.addcustomer()
        print("CUSTOMER ADDED SUCESSFULLY")
    elif(choice=="2"):
        ob=customer()
        ob.id=input("enter id to search")
        ob.searchcustomer()
        showcustomer(ob)
    elif(choice=="3"):
        ob=customer()
        ob.id=input("enetr id to delete data")
        flag=ob.deletecustomer()
        if(flag):
            print("deleted sucessfully")
        else:
            print("invalid i'd")


    elif(choice=="4"):
        ob=customer()
        ob.id=input("enetr id to modify data")
        ob.name=input("enter name")
        ob.age=input("enter age")
        ob.mobile=input("enter mobile num")
        ob.modifycustomer()

    elif(choice=="5"):

        ob=customer()
        for e in customer.STORAGE:
            showcustomer(e)

    else:
        print("Thanks for using CMS")

