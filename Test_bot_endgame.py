#!/usr/bin/env python
# coding: utf-8

# In[1]:


import unittest

from main_package.Stock_main import *
#from main_package.Buy import *
#from sub_package.User import *
from sub_package.bot import *
#from sub_package.endgame import *


# In[4]:


class Testbot(unittest.TestCase): # test class
    
    @classmethod
    def setUpClass(cls):
        print('setupClass')
    
    def setUp(self):
        print('Set up')
        
    def tearDown(self):
        print('Tear Down')

    def test_bot_buy(self): # test case
        
        Stock1 = Stock()
        U2 = bot(Stock1)
        
        container_price = list(range(50,201))
        
        output = U2.buy_stock_rp(201, 50, vol=10)
         
        self.assertEqual(output[0],(10*output[1]))
        
        self.assertEqual(output[2],10)
        #try with 100, there will be assertion error
        
        self.assertIn(output[1],container_price)
        
    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

        
        
unittest.main(argv=[''], verbosity=2, exit=False)


# In[ ]:




