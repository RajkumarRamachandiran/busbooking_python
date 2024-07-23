import time
import pywhatkit
import random   
print("-------------------------------------------------------------------------------------------")
print("  "                        "welcom to vijay cinemas  "                                   " ")
print("-------------------------------------------------------------------------------------------")
time.sleep(1)
print("1)login")
print("2)register")
time.sleep(1)
option=int(input("enter the login option:"))
if(option==1 ):
    username=input("email:")
    password=input("password:")
    print("login sucessfully")
elif(option==2):
    name=input("name:")
    phone_no=input("phone_no:")
    email=input("email:")
else:
    print("first register you profile")
#     otp=random.randint(1000,9999)
#     message='dear:{name} thank you for register vijay cinemas and your otp is {otp}.'
    
# pywhatkit.send_mail(phone_no,message)
    while True:
       creat_password=input("create_password:")
       confirm_password=input("confirm_password")
       if creat_password==confirm_password:
          print("register sucessfully..")
          break
       else:
            print("wrong password retry!")


movies={
    "1":{"moviename":"leo","price":120},
    "2":{"moviename":"star","price":120},
    "3":{"moviename":"master","price":150},
    "4":{"moviename":"maharaja","price":130}
}

for key,movie in movies.items():
    print(f"{key}.{movie['moviename']} - RS{movie['price']} per ticket")

movies_choice=input("enter the movie number:")

if movies_choice in movies:
      selected_movie=movies[movies_choice]
      print(f"You selected {selected_movie['moviename']}")
      if movies_choice == str(1):
          print("show time 10:30AM")
          print(" available seat 30")
      elif movies_choice==str(2):
          print("show time 2:30pm")
          print("avaliable seat 70")
      elif movies_choice==str(3):
          print("show time 5:30pm")
          print("avaliable ticket 100")
      elif movies_choice==str(4):
          print("show time 8:00 pm")
          print(" avaliable seat 49")
      num_tickets = int(input("Enter the number of tickets you want to purchase: "))
    
      if num_tickets > 0:
          total_cost = selected_movie['price'] * num_tickets
          print(f"Total cost for {num_tickets} tickets to {selected_movie['moviename']} is Rs{total_cost}")
      else:
          print("Invalid number of tickets. Please enter a positive number.")
else:
     print("Invalid movie selection. Please restart and select a valid movie.")





    
    
