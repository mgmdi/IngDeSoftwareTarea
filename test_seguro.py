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


    def test_verificacionDatosNF(self):

        self.assertEqual(Tarea2.verificacionDatos(56,"f",800,False), "SI")
        self.assertEqual(Tarea2.verificacionDatos(70,"m",50,False), "NO")
        self.assertEqual(Tarea2.verificacionDatos(80,"f",1000,False), "SI")
        self.assertEqual(Tarea2.verificacionDatos(50,"f",800,False), "NO")
        self.assertEqual(Tarea2.verificacionDatos(40,"m",500,False), "NO")
        self.assertEqual(Tarea2.verificacionDatos(63,"f",800,False), "SI")
        self.assertEqual(Tarea2.verificacionDatos(78,"f",600,False), "NO")
        self.assertEqual(Tarea2.verificacionDatos(66,"m",800,False), "SI")
        self.assertEqual(Tarea2.verificacionDatos(58,"m",800,False), "SI")
        self.assertEqual(Tarea2.verificacionDatos(40,"f",800,False), "SI")


    def test_verificacionDatosF(self):
        """
        Funcion con casos frontera.
        Los casos frontera se definen como la minima edad y minimo numero de cotizaciones
        que se debe tener para optar por el seguro.
        Se considera la minima edad como 55 para hombres (con 5 anos maximos de disminucion por trabajo
        en medios insalubres) y 50 para las mujeres por la misma razon. 
        """

        self.assertEqual(Tarea2.verificacionDatos(55,"f",750,True), "SI")
        self.assertEqual(Tarea2.verificacionDatos(50,"f",750,True), "SI")
        self.assertEqual(Tarea2.verificacionDatos(60,"m",750,True), "SI")
        self.assertEqual(Tarea2.verificacionDatos(55,"m",750,True), "SI")
        

if __name__ == '__main__':
    unittest.main()  