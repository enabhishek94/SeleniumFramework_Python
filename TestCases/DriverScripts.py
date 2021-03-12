import unittest

def run(test):
    loader = unittest.TestLoader()
    loader.discover("test_01.py")