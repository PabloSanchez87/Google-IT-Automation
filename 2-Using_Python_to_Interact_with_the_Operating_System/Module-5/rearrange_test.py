#!/usr/bin/python3

import unittest

from rearrange import rearrange_name

class TestRearrange(unittest.TestCase):
    
  def test_basic(self):
    testcase = "Lovelace, Ada"
    expected = "Ada Lovelace"
    self.assertEqual(rearrange_name(testcase), expected)
    
# Ejecuta las pruebas con más detalles
if __name__ == "__main__":
    unittest.main(verbosity=2)