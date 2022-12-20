import unittest

from main_package.Stock_main import *

class TestUser(unittest.TestCase): # test class
      
      @classmethod
      def setUpClass(cls):
            print('setupClass')
      
      def setUp(self):
            print('Set up')

      def test_high_price(self):
            self.high_price_list = [20,30,40]
            # self.low_price_list = [5,10,15]
            # self.volume_list = [1,2,3]
            self.assertEqual(self.get_high_price, self.high_price_list)
            
      def test_low_price(self):
            # self.high_price_list = [20,30,40]
            self.low_price_list = [5,10,15]
            # self.volume_list = [1,2,3]
            self.assertEqual(self.get_low_price, self.low_price_list)
            
      def test_high_price(self):
            self.high_price_list = [20,30,40]
            # self.low_price_list = [5,10,15]
            # self.volume_list = [1,2,3]
            self.assertEqual(self.get_high_price, self.high_price_list)
            
      def tearDown(self):
            print('Tear Down')
      
      @classmethod
      def tearDownClass(cls):
            print('teardownClass')
            