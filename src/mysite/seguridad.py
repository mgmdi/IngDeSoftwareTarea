import re

class Seguridad:


    def __init__(self):
        self.usuariosRegistrados = {}


    def registrarUsuario(self, username, email, password1, password2):

        correoValido = self.checkEmail(email)
        passwordsIguales = self.coincidePasswords(password1,password2)
        sinCaracteresEspeciales = self.checkSpecialChar(password1)
        contrasenaValida = self.coincidePasswords(password1,password2)

        if correoValido:
            if passwordsIguales and sinCaracteresEspeciales and contrasenaValida and self.checkLength(password1):
                clave = self.claveCodificada(password1)
                self.usuariosRegistrados[email] = clave
                return True

        return False


    def ingresarUsuario(self, correo, clave):

        userValido = False
        claveValida = False
        for email in self.usuariosRegistrados:
            if correo == email:
                userValido = True
                if self.usuariosRegistrados[email] == self.claveCodificada(clave):
                    claveValida = True

        if not userValido:
            return "User invalido"
        elif not claveValida:
            return "Clave invalida"
        else:
            return True


    def coincidePasswords(sefl, password1, password2):
        return password1 == password2
        

    def checkLength(self,password):
        return len(password) in range(8,17)
        

    def checkSpecialChar(self, password):
        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]') 
        return(regex.search(password) == None)
         

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
        if re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email) == None:
            return False
        return True
        
    
    def claveCodificada(self, password):
        return password[::-1] 
        

    