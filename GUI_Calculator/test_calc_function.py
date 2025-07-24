import unittest
import shared_variables
import calc_function
import tkinter as tk

class TestCalcFunctions(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()
        shared_variables.calculation = "None"
        shared_variables.value = tk.StringVar()
        shared_variables.prev_result = tk.StringVar()

    def tearDown(self):
        self.root.destroy()

    def test_zero(self):
        shared_variables.calculation = "None"
        calc_function.zero()
        self.assertEqual(shared_variables.value.get(),'0')
        
    def test_one(self):
        shared_variables.calculation = "None"
        calc_function.one()
        self.assertEqual(shared_variables.value.get(),'1')
        
    def test_two(self):
        shared_variables.calculation = "None"
        calc_function.two()
        self.assertEqual(shared_variables.value.get(),'2')
        
    def test_three(self):
        shared_variables.calculation = "None"
        calc_function.three()
        self.assertEqual(shared_variables.value.get(),'3')
        
    def test_four(self):
        shared_variables.calculation = "None"
        calc_function.four()
        self.assertEqual(shared_variables.value.get(),'4')
        
    def test_five(self):
        shared_variables.calculation = "None"
        calc_function.five()
        self.assertEqual(shared_variables.value.get(),'5')
        
    def test_six(self):
        shared_variables.calculation = "None"
        calc_function.six()
        self.assertEqual(shared_variables.value.get(),'6')
        
    def test_seven(self):
        shared_variables.calculation = "None"
        calc_function.seven()
        self.assertEqual(shared_variables.value.get(),'7')
        
    def test_eight(self):
        shared_variables.calculation = "None"
        calc_function.eight()
        self.assertEqual(shared_variables.value.get(),'8')
        
    def test_nine(self):
        shared_variables.calculation = "None"
        calc_function.nine()
        self.assertEqual(shared_variables.value.get(),'9')
        
    def test_equal(self):
        shared_variables.calculation = "1+2"
        calc_function.equal()
        self.assertEqual(shared_variables.value.get(),"3.0")
        self.assertEqual(shared_variables.prev_result.get(),"1+2 = 3.0")
    
    def test_dot(self):
        shared_variables.calculation = "None"
        calc_function.dot()
        self.assertEqual(shared_variables.value.get(),"0.")
        
    def test_left_par(self):
        shared_variables.calculation = "None"
        calc_function.left_par()
        self.assertEqual(shared_variables.value.get(),"(")
        
    def test_right_par(self):
        shared_variables.calculation = "None"
        calc_function.right_par()
        self.assertEqual(shared_variables.value.get(),"()")
        
    def test_percent(self):
        shared_variables.calculation = "None"
        calc_function.percent()
        self.assertEqual(shared_variables.value.get(),"0/100")
        
    def test_plus(self):
        shared_variables.calculation = "3"
        calc_function.plus()
        self.assertEqual(shared_variables.value.get(),"3+")
        
    def test_minus(self):
        shared_variables.calculation = "3"
        calc_function.minus()
        self.assertEqual(shared_variables.value.get(),"3-")
        
    def test_divison(self):
        shared_variables.calculation = "0"
        calc_function.division()
        self.assertEqual(shared_variables.value.get(),"0/")
        
    def test_times(self):
        shared_variables.calculation = "4"
        calc_function.times()
        calc_function.two()
        self.assertEqual(shared_variables.value.get(),"4*2")
        
    def test_AllClear(self):
        shared_variables.calculation = "100"
        calc_function.AllClear()
        self.assertEqual(shared_variables.value.get(),"None")

if __name__ == '__main__':
    unittest.main()