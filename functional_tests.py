from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_lims(self):

        # Ruben access the LIMS site
        self.browser.get('http://localhost:8000')

        # Notices the title is what he expects
        self.assertIn('LIMS', self.browser.title)

        self.fail('Finish the test!')

        # He would like to do the following tasks inside
        # the system:

        # - Be able to create plates (and their wells), sample tubes
        # and library tubes
        # - Add and remove sample(s) from a container
        # - Move sample(s) from one container to another
        # - Add tags to samples
        # - Search for a container by its barcode
        # - Obtain a list of samples (and tags) for a plate or tube

        # Once he's donde that he can go home and do what he likes best:
        # relax and watch TV (whilst learning new programing languages)

if __name__ == '__main__':
    unittest.main(warnings='ignore')
