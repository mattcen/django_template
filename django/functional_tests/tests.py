#!/usr/bin/env python
import unittest

from selenium import webdriver


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_django(self):
        # Edith has heard about a cool new online app
        # She goes to check out its homepage
        self.browser.get("http://localhost:8000")

        # She notices the page title and header mention Django
        self.assertIn("Django", self.browser.title)

        # She is invited to get started
        self.fail("Finish the test!")

        # Satisfied, she goes back to sleep


if __name__ == "__main__":
    unittest.main()
