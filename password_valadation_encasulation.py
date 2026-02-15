class user:
    def __init__(self):
        self.__password = None
    def set_password(self,pwd):
        if(len(pwd)) >= 6:
            self.__password == pwd
            print("password entered successfully...")
        else:
            print("password must be greater or equal to six characters")
    def check_password(self,pwd):
        if self.__password == pwd:
            print("access granted")
        else:
            print("access denied")
user1 = user()
password = input("enter your password:")
user1.set_password(password)
login = input("enter password to login:")
user1.check_password(login)
