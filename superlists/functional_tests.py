from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        # no proxy
        self.profile = webdriver.FirefoxProfile()
        self.profile.set_preference('network.proxy.type', 0)
        self.profile.update_preferences()

        self.browser = webdriver.Firefox(firefox_profile=self.profile)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main()
