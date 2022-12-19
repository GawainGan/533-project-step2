import unittest

from main_package.Stock_main import *

class TestUser(unittest.TestCase): # test class
      
      @classmethod
      def setUpClass(cls):
            print('setupClass')
      
      def setUp(self):
            print('Set up')

            
      def tearDown(self):
            print('Tear Down')
      
      @classmethod
      def tearDownClass(cls):
            print('teardownClass')
            