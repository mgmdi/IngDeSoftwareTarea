import re

class Seguridad:


    def __init__(self):
        usuariosRegistrados = {}


    def registrarUsiario(self, email, password1, password2):




    def coincidePasswords(sefl, password1, password2):
        return password1 == password2
        

    def checkLength(self,password):
        return len(password) in [8,16]
        


    def checkSpecialChar(self, password):
 
        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]') 
         
        if(regex.search(password) == None): 
            print("String is accepted") 
            
        else: 
            print("String is not accepted.") 

    def validPassword(self, password):




    def checkEmail(self, email):
        return re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email)
    
    
        

    