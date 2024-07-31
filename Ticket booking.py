#login page
print("___________Welcome To Fast&Safe Bus__________")
print("__________Bus Ticket Booking__________")
print("Sign up")
username=input("username:")
age=int(input("userage:"))
gender=input("male/female/other:")
email=input("email:")
number=int(input("Enter Your Mobile Number:"))
while True:
    password=input("password:")
    re_password=input("re_enter password:")
    if password==re_password:
         print("SUCCESSESFULLY REGISTER")
         break
    else:
        print("Both Password Or Not Same")    
print("Sign in")
while True:
    login=input("username:")
    login_pass=input("password:")
    if (username==login and password==login_pass):
         print("SIGN IN SUCCESSFULLY")
         break
    else:
         print("username or password is wrong") 
#booking page
print("!!!!!BOOK NOW!!!!!")
class route1():
    def chennai_to_trichy(self):
        from_=input("From:")      
        to_=input("to:")
        if(from_=="chennai" and to_=="trichy"):
            print("bus:301 Time:8:30am","Rs600")
        elif(from_=="chennai" and to_=="ulundurpet"):
            print("bus:301 Time:8:30am","Rs500")
        elif(from_=="chennai" and to_=="villuppuram"):
            print("bus:301 Time:8:30am","Rs450")
        elif(from_=="chennai" and to_=="thindivanam"):
            print("bus:301 Time:8:30am","Rs400")
        elif(from_=="chennai" and to_=="melmaruvathur"):
            print("bus:301 Time:8:30am","Rs350")
        elif(from_=="chennai" and to_=="chengalpet"):
            print("bus:301 Time:8:30am","Rs300")
        elif(from_=="chennai" and to_=="kilambakkam"):
            print("bus:301 Time:8:30am","Rs250")
        else:
            print("enter your correct route")
class route2(route1):
    def chennai_to_pudhuchery(self):
        print("!!!!!BOOK NOW!!!!!")
        while True:
            from_=input("From:")      
            to_=input("to:")
            if(from_=="chennai" and to_=="pudhuchery"):
                print("bus:302 Time:8:30am","Rs600")
            elif(from_=="chennai" and to_=="marakkanam"):
                print("bus:302 Time:8:30am","Rs500")
            elif(from_=="chennai" and to_=="kuvathur"):
                print("bus:302 Time:8:30am","Rs450")
            elif(from_=="chennai" and to_=="kalpakkam"):
                print("bus:302 Time:8:30am","Rs400")
            elif(from_=="chennai" and to_=="mamallalapuram"):
                print("bus:302 Time:8:30am","Rs350")
            elif(from_=="chennai" and to_=="navalur"):
                print("bus:302 Time:8:30am","Rs300")
                break
            else:
                print("enter your correct route")
class route3(route2):
    def chennai_to_madurai(self):
        print("!!!!!BOOK NOW!!!!!")
        from_=input("From:")      
        to_=input("to:")
        if(from_=="chennai" and to_=="madurai"):
            details={"bus_no":"303",
                     "time":"8.30",
                     "amount":"1000"}
            print(details)
            while True:
                amount=int(input("pay the amount for ticket booking:"))
                if amount==1000:
                    print("payment succesfully!")
                    print("your ticket is booked")
                    break
                else:
                    print(" payment is wrong pay the correct amount and confirm your ticket")
        elif(from_=="chennai" and to_=="trichy"):
            print("bus:303 Time:8:30am","Rs600")
        elif(from_=="chennai" and to_=="perambalur"):
            print("bus:303 Time:8:30am","Rs450")
        elif(from_=="chennai" and to_=="ulundurpet"):
            print("bus:303 Time:8:30am","Rs400")
        elif(from_=="chennai" and to_=="dindukkal"):
            print("bus:303 Time:8:30am","Rs350")
        elif(from_=="chennai" and to_=="villupuram"):
            print("bus:303 Time:8:30am","Rs300")
        else:
            print("enter your correct route")
obj=route3()
print("1) chennai to trichy")
print("2) chennai to pudhuchery")
print("3)chennai_to_madurai")
while True:
    route=int(input("enter the root:"))
    if route==1:
        obj.chennai_to_trichy()
    elif route ==2:
        obj.chennai_to_pudhuchery()
    elif route==3:
        obj.chennai_to_madurai()
        break
    else:
     print("choose the correct route")



    
        







    





    
