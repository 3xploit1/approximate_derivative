from sympy import * 

class Solve():
    def __init__(self):
        self.h = 1e-5
        
    def func(self, val: int | float, flag: int):
        '''
        Ввод целевой функции
         
        Аргумент функции Symbol — строка, содержащая символ, который можно присвоить переменной.
        
        Метод sympify класса sympy преобразует введенное строковое выражение в математическое. 
        С помощью метода subs появляется возможность подставлять значения в математическое выражение
        '''
        if (flag == 1):
            x = symbols('x')    
            print('[----Ручной ввод----]')
            return sympify(input('Функция: ')).subs(x, val)
        if (flag == 2): 
            return 3*val**2 # aka 3x^2
        
    def solve(self, x: int | float, flag: int):
        '''
        Метод вычисления проивзодной функции заданной в конечном числе точек
        
        Формула: https://ru.wikipedia.org/wiki/Численное_дифференцирование
        
        - func: входная функция 
        - x: значение функции (точка)
        - h: шаг, должен быть малым `1e-5 = 0,00001`
        
        flag
            `1 - Ручной ввод`
            
            `2 - Фиксированный`
        '''

        return round(float(self.func((x + self.h), flag) - self.func((x - self.h), flag)) / (2 * self.h),4)
