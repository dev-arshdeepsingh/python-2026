'''
username = "arshdeep"
password = 1234
chance = 0
while chance <3:
    name = input("Enter Username: ")
    pin = int(input("Enter 4 digits PIN: "))

    if name == username and pin == password:
        print("Login Successful")
        break
    else:
        print("Login Failed! Try Again")
        if chance == 0:
            for i in range(0,101):
                print(i)
        elif chance == 1:
            for i in range(0,500):
                print(i)
        elif chance == 2:
            print("You're are blocked!")


    chance +=1
'''  

#``````````````````````````````````````````````````````````````````````````````````````````
'''
import time  
username = 'arshdeep'
login_attempt = 1
max_attempts = 3
wait_time = 10

while login_attempt <= max_attempts:
    name = input("Enter Username: ")
    if name == username:
        print("Login Successful")
        break
    else:
        print("Login Failed!--attempt no.: ", login_attempt, "--Wait time: ", wait_time)
        time.sleep(wait_time)
        login_attempt +=1
        wait_time *= 3
'''

#---------------------------------------------------------------------------------------


import time

attempt = 1
wait_time = 10
pin = 123456

while attempt<=3:
    key = int(input("Enter 6 digts pin: "))
    if attempt ==1:
        if key == pin:
            print("Login Success")
            break
        else:
            print("Wrong PIN!")
    elif attempt == 2:
        if key == pin:
            print("Login Success")
            break
        else:
            print("Wrong PIN!")
    elif attempt == 3:
        if key == pin:
            print("Login Success")
            break
        else:
            print("Wrong PIN! You are Blocked")
    print("Wait Time = ", wait_time)
    time.sleep(wait_time)
    wait_time *= 2
    attempt += 1





