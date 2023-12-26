import unittest 
from name_function import get_formatted_name 

class NamesTestCase(unittest.TestCase): 
    """Tests for 'name_function.py'.""" 
    
    def test_first_last_name(self): 
        """Do names like 'Janis Joplin' work?""" 
        formatted_name = get_formatted_name('janis', 'joplin') 
        self.assertEqual(formatted_name, 'Janis Joplin') 
        
    # Comment out this test after running previous and making necessary adjustment in the function
    # def test_first_last_middle_name(self): 
    #     """Do names like 'Wolfgang Amadeus Mozart' work?""" 
    #     formatted_name = get_formatted_name( 'wolfgang', 'mozart', 'amadeus') 
    #     self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')


if __name__ == '__main__': 
    unittest.main()