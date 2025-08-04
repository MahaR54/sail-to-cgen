import unittest
from parser import convert_yaml_to_sexpr

class TestParser(unittest.TestCase):
    def test_simple(self):
        yaml = "key: value"
        output = convert_yaml_to_sexpr(yaml)
        self.assertIn('(yaml:key "value")', output)

if __name__ == "__main__":
    unittest.main()
