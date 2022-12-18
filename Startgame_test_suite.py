#!/usr/bin/env python
# coding: utf-8

# In[3]:


import unittest
from Test_bot_endgame import *
#from TestModule2 import TestSub
def my_suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    #add for each of the py files created with test case
    suite.addTest(unittest.makeSuite(Testbot))
#    suite.addTest(unittest.makeSuite(TestSub))
    #runner = unittest.TextTestRunner()
    return suite
    
#print(runner.run(suite))

#my_suite()


# In[5]:


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(my_suite())


# In[ ]:




