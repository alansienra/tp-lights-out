#Aca voy a realizar una prueba usando el mudolo unitest
import unittest
import usuario

class UsuarioTest(unittest.TestCase):

    def testSaludarDeberiaDevolverHola(self):

        #ARRANGE
        saludoEsperado = "Hola"

        #ACT
        saludoRecibido = usuario.saludar()

        #ASSERT
        self.assertEqual(saludoEsperado,saludoRecibido)