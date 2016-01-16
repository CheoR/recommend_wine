from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_post_a_review_and_see_it_later(self):

        # Sara likes wine. So she heads overs to the wine's home page.
        self.browser.get('http://localhost:8000')

        # And notcies the wine's title in the corder along with some other
        # details about wines choses by users along with their ratings.
        self.assertIn('RecommendWine', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('RecommendWine', header_text)

        # She notices the comment section.
        inputbox = self.browser.find_element_by_id('id_new_comment')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter your comment here'
        )

        # And adds that she likes red wines
        inputbox.send_keys('I like red wines.')

        # After hitting enter, the page updates and shoes her comment
        table = self.browser.find_element_by_id('id_comments_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: I like red wines.' for row in rows),
            "New comments did not appear in table"
        )

        # She selects a rating using the raiting selector

        # And adds a little bit to the comment box.

        # Clicking on the Add button she notices that the reviws
        # and ratings for her chosen wine has updated.

        # Satisfied she opens up another bottle to review.
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')