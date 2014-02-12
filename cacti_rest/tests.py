#This file mainly exists to allow python setup.py test to work.
import unittest, os, subprocess, logging
from cacti_rest.rra import extract_data, convert_to_json
from cacti_rest.models import Settings


RRA_TEST = "/home/raton/komodo_work/iberia/cacti_rest/cacti_rest/cacti_rest/test.rrd"

class TestRra(unittest.TestCase):
    def setUp(self):
        logging.basicConfig(level=logging.DEBUG)
        Settings(name="path_rrdtool", value="/usr/bin/rrdtool").save()
        
    def test_export(self, ):
        print extract_data(RRA_TEST, 300, "-1h")
    
    def test_convert_to_json(self):
        print convert_to_json(extract_data(RRA_TEST, 300, "-1h"))

        

def main():
    
    unittest.main()

if __name__ == "__main__":
    unittest.main()
