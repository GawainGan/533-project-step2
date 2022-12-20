import unittest

from main_package.Stock_main import *

class TestStock(unittest.TestCase): # test class
      
      @classmethod
      def setUpClass(cls):
            print('setupClass')
      
      def setUp(self):
            print('Set up')

      def test_high_price(self):
            self.high_price_list = [20,30,40]
            self.assertEqual(self.high_price_list, [20,30,40])
            
      def test_low_price(self):
            self.low_price_list = [5,10,15]
            self.assertEqual(self.low_price_list, [5,10,15])
            
      def test_vol(self):
            self.volume_list = [1,2,3]
            self.assertEqual(self.volume_list, [1,2,3])
      
      def test_size(self):
            self.n = 5
            self.high_price_list = [random.randint(201, 500) for i in range(int(self.n))]
            self.low_price_list = [random.randint(50, 200) for i in range(int(self.n))]
            self.volume_list = [random.randint(1, 200) for i in range(int(self.n))]
            self.assertEqual(self.n , len(self.high_price_list()))
            self.assertEqual(self.n , len(self.low_price_list()))
            self.assertEqual(self.n , 4) # it will has error
            
            
            
      def tearDown(self):
            print('Tear Down')
      
      @classmethod
      def tearDownClass(cls):
            print('teardownClass')