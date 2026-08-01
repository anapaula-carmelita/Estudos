import unittest

from lab_14_point import Point

class TestPoint(unittest.TestCase):

    def test_inicializacao_padrao(self):
        """Testa se o ponto é criado na origem (0,0) por padrão."""
        p = Point()
        self.assertEqual(p.getx(), 0.0)
        self.assertEqual(p.gety(), 0.0)

    def test_inicializacao_com_valores(self):
        """Testa se o ponto guarda corretamente as coordenadas passadas."""
        p = Point(3.5, 4.2)
        self.assertEqual(p.getx(), 3.5)
        self.assertEqual(p.gety(), 4.2)

    def test_distance_from_xy(self):
        """Testa o cálculo da distância passando x e y diretamente."""
        p = Point(1.0, 2.0)
        # Distância entre (1,2) e (4,6) é 5.0
        self.assertAlmostEqual(p.distance_from_xy(4.0, 6.0), 5.0)

    def test_distance_from_point(self):
        """Testa o cálculo da distância passando outro objeto Point."""
        p1 = Point(1.0, 2.0)
        p2 = Point(4.0, 6.0)
        # A distância de p1 para p2 deve ser 5.0
        self.assertAlmostEqual(p1.distance_from_point(p2), 5.0)

    def test_distancia_zero(self):
        """Testa a distância de um ponto para ele mesmo (deve ser 0)."""
        p = Point(5.0, -3.0)
        self.assertEqual(p.distance_from_xy(5.0, -3.0), 0.0)

    def test_distancia_com_coordenadas_negativas(self):
        """Garante que o cálculo funciona nos quadrantes negativos."""
        p1 = Point(-2.0, -3.0)
        p2 = Point(-5.0, -7.0)
        # Distância entre (-2,-3) e (-5,-7) é 5.0
        self.assertAlmostEqual(p1.distance_from_point(p2), 5.0)

if __name__ == '__main__':
    unittest.main()