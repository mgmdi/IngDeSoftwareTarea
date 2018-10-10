import unittest
import Tarea2

class TestSeguro(unittest.TestCase):

    def test_calculoEdad(self):

        self.assertEqual(Tarea2.calculoEdad("16/06/1997"), 21)
        self.assertEqual(Tarea2.calculoEdad("16/06/1980"), 38)
        self.assertEqual(Tarea2.calculoEdad("16/12/1998"), 20)
        self.assertEqual(Tarea2.calculoEdad("09/10/1998"), 21)
        self.assertEqual(Tarea2.calculoEdad("16/06/1998"), 21)
        self.assertEqual(Tarea2.calculoEdad("10/10/1970"), 47)
        self.assertEqual(Tarea2.calculoEdad("01/01/1950"), 68)
        self.assertEqual(Tarea2.calculoEdad("15/06/1960"), 58)
        self.assertEqual(Tarea2.calculoEdad("25/07/1956"), 62)
        self.assertEqual(Tarea2.calculoEdad("30/12/1940"), 77)  


    def test_verificacionDatos(self):
        
        self.assertEqual(Tarea2.verificacionDatos(56,"f",800), "SI")
        self.assertEqual(Tarea2.verificacionDatos(70,"m",50), "NO")
        self.assertEqual(Tarea2.verificacionDatos(80,"f",1000), "SI")
        self.assertEqual(Tarea2.verificacionDatos(50,"f",800), "NO")
        self.assertEqual(Tarea2.verificacionDatos(40,"m",500), "NO")
        self.assertEqual(Tarea2.verificacionDatos(63,"f",800), "SI")
        self.assertEqual(Tarea2.verificacionDatos(78,"f",600), "NO")
        self.assertEqual(Tarea2.verificacionDatos(66,"m",800), "SI")
        self.assertEqual(Tarea2.verificacionDatos(58,"m",800), "SI")
        self.assertEqual(Tarea2.verificacionDatos(40,"f",800), "SI")



if __name__ == '__main__':
    unittest.main()  