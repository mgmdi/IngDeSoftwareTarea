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
        mayus = 0
        minus = 0
        digitos = 0
        listMin = list(string.ascii_lowercase)
        listMayus = list(string.ascii_uppercase)
        for c in password:
            if c in listMayus:
                mayus += 1
            elif c in listMin:
                minus += 1
            elif c in [0,9]:
                digitos += 1

        if mayus + minus >= 3 and minus > 0 and mayus > 0 and digitos > 0:
            return True

        else:
            return False




    def checkEmail(self, email):
        return re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email)
    
    
        

    