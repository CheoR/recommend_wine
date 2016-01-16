from django.template.loader import render_to_string
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.test import TestCase

from reviews_app.views import home_page

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
        request.POST['comment_text'] = 'A new comment'

        response = home_page(request)

        self.assertIn('A new comment', response.content.decode())

        self.assertIn('A new comment', response.content.decode())
        expected_html = render_to_string(
            'home.html',
            {'new_comment_text':  'A new comment'}
        )
        self.assertEqual(response.content.decode(), expected_html)