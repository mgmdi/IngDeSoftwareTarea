import unittest
import seguridad as sec

global seguridad
seguridad = sec.Seguridad()

class TestBeta(unittest.TestCase):

    
    
    

    def test_registrarUsuario(self):
        self.assertEqual(seguridad.registrarUsuario("mgmdi","mjgf@gmail.com","mmM123MJ","mmM123MJ"), True)
        self.assertEqual(seguridad.registrarUsuario("mgmdi","mjgf@gmail.com","mmM123MJ","mmMMJ"), False)
        self.assertEqual(seguridad.registrarUsuario("mgmdi","mjgfgmail.com","mmM123MJ","mmM123MJ"), False)
        self.assertEqual(seguridad.registrarUsuario("mgmdi","mjgf@gmail.com","mmM123MJ","mmM13MJ"), False)
        self.assertEqual(seguridad.registrarUsuario("mgmdi","mjgf@gmail.com","123MJ","123MJ"), False)
        self.assertEqual(seguridad.registrarUsuario("mgmdi","mjgf@gmail","123MJmmw","123MJmmw"), False)

    def test_ingresarUsuario(self):
        self.assertEqual(seguridad.ingresarUsuario("mjgf@gmail.com","mmM123MJ"), True)


if __name__ == '__main__':
    unittest.main() 