# Импортируем тест-кейсы и модуль unittest
import unittest
import module_12_1
import module_12_2

# Создадим тест-сьют
testSUITE = unittest.TestSuite()
testSUITE.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_1.RunnerTest))
testSUITE.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_2.TournamentTest))

runn_ = unittest.TextTestRunner(verbosity=2)
runn_.run(testSUITE)