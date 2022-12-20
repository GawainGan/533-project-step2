import unittest

from main_package.Stock_main import *
from sub_package.User import *

class TestUser(unittest.TestCase): # test class
      
      
      
      @classmethod
      def setUpClass(cls):
            print('setupClass')
      
      def setUp(self):
            print('Set up')

            
      def tearDown(self):
            print('Tear Down')

      
      def test_buy_stock_rp(self): # test case
            

            Stock1 = Stock()
            U1 = User(Stock1)
            
            container_price_min = list(range(50,201))
            container_price_max = list(range(200,500))
            
            output = U1.Buy.buy_stock(high_price = 50, low_price = 10,  vol = 1)
            # output: info.append(total_price) , info.append(buy_price), info.append(buy_volume)
      
            self.assertEqual(output[0],(output[1]* output[2]))
            
            self.assertEqual(output[2],10)
            #try with 100, there will be assertion error
            
            self.assertIn(output[1],container_price_min)
            
            output = U1.Buy.buy_stock(high_price = 80, low_price = 20,  vol = 5) 
            # output: info.append(total_price) , info.append(buy_price), info.append(buy_volume)
            self.assertIn(output[1],container_price_max)

      def test_get_expense_list(self): # test case
            Stock1 = Stock()
            U1 = User(Stock1)
            
            U1.process()
            
            out_expense = U1.get_expense_list()
            print(sum(out_expense))
            
            testval = (sum(out_expense) <= 10000.0)
            
            self.assertTrue(testval,"Expense > 10000")

      @classmethod
      def tearDownClass(cls):
            print('teardownClass')