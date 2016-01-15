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

        assert 'RecommendWine' in self.browser.title, "Browser title was " + self.browser.title

        # She notices that there's also an option to add her own wine rating and review

        # She selects a rating using the raiting selector

        # And adds a little bit to the comment box.

        # Clicking on the Add button she notices that the reviws and ratings for her
        # chosen wine has updated.

        # Satisfied she opens up another bottle to review.
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')