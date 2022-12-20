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