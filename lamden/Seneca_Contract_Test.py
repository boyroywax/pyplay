#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataSciece.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'lamden'))
	print(os.getcwd())
except:
	pass

#%%
from seneca.tooling import export, publish_function

def my_first_contract():
    @export
    def add(x, y):
        return x + y


#%%
contract = publish_function(my_first_contract, 
    name='first_contract',
    author='stu')

contract.add(x=1, y=2)


#%%
from seneca.tooling import export, publish_function

def my_first_contract():
    @export
    def add(x, y):
        return x + y
        
contract = publish_function(my_first_contract, 'first_contract', 'stu')

assert contract.add(x=1, y=2)['output'] == 3


#%%
import unittest
from unittest import TestCase, main
from seneca.tooling import export, publish_function

CONTRACT_NAME = 'first_contract'
CONTRACT_AUTHOR = 'stu'

def my_first_contract():
    @export
    def add(x, y):
        return x + y

class TestBasicAddition(TestCase):
    def setUp(self):
        # See if the contract has already been submitted by trying to pull it.
        # If this fails, submit it.
        try:
            self.contract = ContractWrapper(CONTRACT_NAME,
                                            default_sender=CONTRACT_AUTHOR)
        except:
            self.contract = publish_function(my_first_contract, 
                                            CONTRACT_NAME,
                                            CONTRACT_AUTHOR)

    def test_addition(self):
        x = 1234
        y = 4321
        output = self.contract.add(x=x, y=y)['output']
        self.assertEqual(output, x + y)

## Below code is used in production        
## main()        

## Below code is used in Jupyter Notebook - https://medium.com/@vladbezden/using-python-unittest-in-ipython-or-jupyter-732448724e31
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)


#%%
from seneca.tooling import default_driver
default_driver.r.flushdb()


