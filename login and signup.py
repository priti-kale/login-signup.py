
import os 
import  re
import json

def check_file(filename):
    if not os.path.exists(filename):
        a=open(filename,"w+")
        a.write("[]")
def read_data(filename):
    b=open(filename,"r")
    c=json.loads(b.read())
    return c
def signup(filename):
    user=input("Enter the user name:-")
    password=input("Enter the password:-")
    if not (re.search("[a-z A-z]",password ) and re.search("[0-9]",password) and re.search("[@#$]",password)):
        print("invalid password") 
        return " "
    com_password=input("comfirm your password:-")
    if password!=com_password:
        print("password did not match")
        return " "
    contact=input("Enter your contact:-")
    if len(contact)==10:
        email=input("enter your email address:-")
        gender=(input("enter youe gender"))
        if gender=="male" or "fimale" or "other":
            age=int(input("enter your age:-"))
            if age<10:
                print("you can't sinup")
        json_data=read_data(filename)
        for u in json_data:
            if u["name"]==user:
                print("user name allready exist")
                return " "
        json_data.append({"name":user,"password":password,"contact":contact,"email":email,"gender":gender,"age":age})
        a=open(filename,"w+")
        b=json.dumps(json_data,indent=2)
        a.write(b)
        print("signup successgully")
    else:
         print("check your contact number")

def login(filename):
    user=input("Enter the user name:-")
    password=input("Enter the password:-")
    json_data=read_data(filename)
    with open(filename,"r") as f:
        json_data=json.load(f)
        for i in json_data:
            # print(i)
            for j in i:
                if i["name"]==user and i["password"]==password:
                    print(i) 
                    print("login successfully") 
                else:
                    print("cheak your password and username")
  

filename="signup.json"
check_file(filename)
print("       WELLCOME TO LOGIN SIGNUP       ")
choice=input("Enter your choice:-if you want to signup so press[1] and you want to login press[2]:-")
if choice=="1":
    signup(filename)
elif choice=="2":
    login(filename)
else:
    print("check your choice")

