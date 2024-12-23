# Импортируем тест-кейсы и модуль unittest
import unittest
import module_12_1_chan
import module_12_2_chan

# Создадим тест-сьют
testSUITE_ch = unittest.TestSuite()
testSUITE_ch.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_1_chan.RunnerTest))
testSUITE_ch.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_2_chan.TournamentTest))

runn_ch = unittest.TextTestRunner(verbosity=2)
runn_ch.run(testSUITE_ch)