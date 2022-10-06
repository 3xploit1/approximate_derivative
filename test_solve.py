import unittest 
import random
from main import Solve
import datetime
from cryptography.fernet import Fernet


class TestSolve(unittest.TestCase):
    
    def setUp(self):
        self.sol = Solve() 
    
    def test_1(self):
        '''
        Проверка на аргумент типа - int 
        Ответ - вверный 
        '''
        self.assertEqual(self.sol.solve(5, 2), 30.0)
    
    def test_2(self):
        '''
        Проверка на аргумент отрицательное число типа - float 
        Ответ - вверный 
        '''
        self.assertEqual(self.sol.solve(-0.3, 2), -1.8)
        
    def test_3(self): 
        '''
        Проверка на ответ со словом test
        '''
        self.assertIsNot(self.sol.solve(3,2),'test')
    
    def test_4(self):
        '''
        Проверка на аргумент строку с числовым значением 
        
        '''
        self.assertEqual(self.sol.solve('1', 2), 6.0)
    
    def test_5(self):
        '''
        Проверка на аргумент типа строка
        '''
        
        self.assertEqual(self.sol.solve('test', 2), 30.6)
    
    def test_6(self):
        '''
        Проверка на аргумент типа bool
        '''
        
        self.assertEqual(self.sol.solve(False, 2), 0.6)
    
    def test_7(self):
        '''
        Проверка поля `шаг`  
        '''
        self.assertEqual(self.sol.h, 1e-5)
        # self.assertEqual(self.sol.solve(, 2), 2.4)
    def test_8(self):
        '''
        Проверка на возврат значения типа float
        '''
        self.assertIsInstance(self.sol.solve(9, 2), float)
    
    def test_9(self):
        '''
        Сравнение 12 с рандомным числом 
        '''
        if ((num:=self.sol.solve(2,2)) == (rand:= random.randint(0,20))): self.assertEqual(num,rand)
        else: self.assertRaises(TypeError)
            
    def test_10(self):
        '''
        Сравнение вернувшегося значения с промежутком от 1 до 100
        '''
        for num in range(1,100):
            if ((num:=self.sol.solve(3,2)) == num):self.assertEqual(num,num)
            else: self.assertRaises(TypeError)
            break
            
    def test_11(self):
        '''
        Провера на тип после изменения типа 
        '''
        
        num = self.sol.solve(4,2) # float 
        num = str(num)
        self.assertIsInstance(num, str)
    
    def test_12(self):
        '''
        Сравнение вернувшегося значения с текущим часом
        '''
        
        # now = datetime.datetime.now().hour()
        if ((num:= self.sol.solve(3,2)) == (hour:= datetime.datetime.now().hour())): self.assertEqual(num, hour) 
        else: self.assertRaises(TypeError)
    
    def test_13(self):
        '''
        Сумма произведения трех чисел и вернувшегося значения
        '''
        num = self.sol.solve(3,2) 
        self.assertEqual(num + (7 * 10 * 2022 ),141558)  #141540 
    
    def test_14(self):
        '''
        Сравнение промежутка с мат выражением
        '''
        num = self.sol.solve(3,2)
        
        if (10 < (num * 2) / 3 < 35): self.assertEqual(num, random.randint(11,35))
        else: self.assertRaises(TypeError)
    
    def test_15(self):
        '''
        Сравнение строки хэша зашифрованного сообшения с строкой полученного числа (строкой)
        '''
        num = str(int(self.sol.solve(1, 2)))
        message = "test"
        key = Fernet.generate_key()
        fernet = Fernet(key)
        encMessage = fernet.encrypt(message.encode())
        enc_str = str(encMessage)
        if (num in enc_str): self.assertIsInstance(num, str)
        else: self.assertRaises(TypeError)
    
if __name__ == "__main__": 
    unittest.main()
    input()
    
    
    