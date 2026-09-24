import json
def login_name():
    try:
        username=input("enter your name: ")
        if not username:
            print("username cannot be empty")
            login_name()
        elif not username.isalpha():
            print("username cannot contain numbers")
            login_name()
        elif login_password(username):
            log_json["user"]=username
            welcome(username)
    except Exception as e:
        print(f"invalid input {e}")
def login_password(usr_name):
    try:
        i=0
        while i<=2:
            password=input("enter the password for %s " % usr_name )
            if len(password) >= 8:
                log_json["passwd"] = password
                return True
            elif len(password) <= 2:
                print("password too short")
                i+=1
            else:
                print("password must contain more than 8 characters")
                i+=1
        if i > 2:
            print("too many attempts, try again afer sometime")
    except Exception as e:
        print(f"invalid input {e}")
    
def welcome(user_name):
    print("hello %s" % user_name)
print("welcome to the app")
log_json = {"user":"",
            "passwd":""}
login_name()
try:
    with open("log.txt","a") as file:
        log_string = json.dumps(log_json,indent =4)
        file.write(log_string+"\n")
except Exception as e:
    print(e)



