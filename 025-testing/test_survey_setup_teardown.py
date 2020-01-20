import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """ Tests for the class AnonymousSurvey"""

    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('\ntearDownClass')

    def setUp(self):
        print('\nSetup')
        self.question = "What language did you first learn to program in?"
        self.my_survey = AnonymousSurvey(self.question)
        self.responses = ['qbasic', 'c', 'c++']

    def tearDown(self):
        print('Tear Down')
        pass

    def test_store_single_response(self):
        """ Test that a single response is stored properly."""
        
        print('test_store_single_response')
        self.my_survey.store_response('qbasic')
        self.assertIn('qbasic', self.my_survey.responses)

    def test_store_three_responses(self):
        """ Test that three individual responses are stored properly."""
       
        print('test_store_three_responses')
        for response in self.responses:
            self.my_survey.store_response(response)

        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

        
if __name__ == '__main__':
    unittest.main()



# Isolate tests, don't make them dependent on each other.

# TDD; write tests before the code