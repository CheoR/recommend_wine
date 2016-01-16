from django.template.loader import render_to_string
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.test import TestCase

from reviews_app.views import home_page
#from reviews_app.models import Comment

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)

        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)

    def test_home_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['review_text'] = 'A new review'

        response = home_page(request)

        self.assertIn('A new review', response.content.decode())

        self.assertIn('A new review', response.content.decode())
        expected_html = render_to_string(
            'home.html',
            {'new_review_text':  'A new review'}
        )
        self.assertEqual(response.content.decode(), expected_html)

class ReviewModelTest(TestCase):
    pass