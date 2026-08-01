import unittest
import math
git add .
git commit -m "Resolvendo conflitos de merge"
from lab_15_triangle import Point, Triangle

# --- TESTES UNITÁRIOS ---

class TestGeometryClasses(unittest.TestCase):

    def test_point_getters(self):
        """Testa se os métodos getx e gety retornam os valores corretos."""
        p = Point(3.5, 4.2)
        self.assertEqual(p.getx(), 3.5)
        self.assertEqual(p.gety(), 4.2)

    def test_point_distance(self):
        """Testa o cálculo da distância entre dois pontos."""
        p1 = Point(0.0, 0.0)
        p2 = Point(3.0, 4.0)
        self.assertAlmostEqual(p1.distance_from_point(p2), 5.0)

    def test_triangle_perimeter_standard(self):
        """Testa o perímetro de um triângulo retângulo clássico (lados 3, 4, 5)."""
        p1 = Point(0.0, 0.0)
        p2 = Point(3.0, 0.0)
        p3 = Point(0.0, 4.0)
        
        triangle = Triangle(p1, p2, p3)
        # 3 + 4 + 5 = 12.0
        self.assertAlmostEqual(triangle.perimeter(), 12.0)

    def test_triangle_perimeter_code_example(self):
        """Testa o perímetro usando o exemplo do código fornecido."""
        triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
        # Lados: 1, 1 e raiz(2) -> 2 + 1.41421356...
        perimetro_esperado = 1.0 + math.sqrt(2.0) + 1.0
        self.assertAlmostEqual(triangle.perimeter(), perimetro_esperado)


if __name__ == "__main__":
    unittest.main()