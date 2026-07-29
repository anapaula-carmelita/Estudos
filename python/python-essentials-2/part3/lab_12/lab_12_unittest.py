import unittest

from lab_12_timer import Timer

class TestTimer(unittest.TestCase):

    def test_str_formatting(self):
        """Testa se a formatação com zeros à esquerda está correta"""
        timer1 = Timer(23, 59, 59)
        self.assertEqual(str(timer1), "23:59:59")
        
        timer2 = Timer(1, 2, 3)
        self.assertEqual(str(timer2), "01:02:03")

    # ---------------------------------------------------------
    # TESTES PARA O MÉTODO: next_second()
    # ---------------------------------------------------------
    def test_next_second_normal(self):
        """Testa o incremento de um segundo normal"""
        timer = Timer(12, 30, 45)
        timer.next_second()
        self.assertEqual(str(timer), "12:30:46")

    def test_next_second_minute_rollover(self):
        """Testa a virada do minuto (segundo 59 -> 00)"""
        timer = Timer(12, 30, 59)
        timer.next_second()
        self.assertEqual(str(timer), "12:31:00")

    def test_next_second_hour_rollover(self):
        """Testa a virada da hora (minuto 59 -> 00)"""
        timer = Timer(12, 59, 59)
        timer.next_second()
        self.assertEqual(str(timer), "13:00:00")

    def test_next_second_day_rollover(self):
        """Testa a virada do dia (23:59:59 -> 00:00:00) - O CASO MAIS CRÍTICO"""
        timer = Timer(23, 59, 59)
        timer.next_second()
        self.assertEqual(str(timer), "00:00:00")

    # ---------------------------------------------------------
    # TESTES PARA O MÉTODO: prev_second()
    # ---------------------------------------------------------
    def test_prev_second_normal(self):
        """Testa o decremento de um segundo normal"""
        timer = Timer(12, 30, 45)
        timer.prev_second()
        self.assertEqual(str(timer), "12:30:44")

    def test_prev_second_minute_rollback(self):
        """Testa a volta do minuto (segundo 00 -> 59)"""
        timer = Timer(12, 30, 0)
        timer.prev_second()
        self.assertEqual(str(timer), "12:29:59")

    def test_prev_second_hour_rollback(self):
        """Testa a volta da hora (minuto 00 -> 59)"""
        timer = Timer(12, 0, 0)
        timer.prev_second()
        self.assertEqual(str(timer), "11:59:59")

    def test_prev_second_day_rollback(self):
        """Testa a volta do dia (00:00:00 -> 23:59:59) - O CASO MAIS CRÍTICO"""
        timer = Timer(0, 0, 0)
        timer.prev_second()
        self.assertEqual(str(timer), "23:59:59")

if __name__ == '__main__':
    unittest.main()