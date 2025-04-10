
import unittest
import script

class TestCapital(unittest.TestCase):

    def test_single_word(self):
        text = 'Vallabh'
        result = script.capitalize_each_letter(text)
        self.assertEqual(result,'VALLABH')

    def test_whole_string(self):
        text = 'Vallabh Rajendra Kulkarni'
        result = script.capitalize_each_letter(text)
        self.assertEqual(result,'VALLABH RAJENDRA KULKARNI')

if __name__ == '__main__':
    unittest.main()
