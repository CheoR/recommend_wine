from django.template.loader import render_to_string
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.test import TestCase

from reviews_app.views import home_page
from reviews_app.models import Review

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

        self.assertEqual(Review.objects.count(), 1)
        new_review = Review.objects.first()
        self.assertEqual(new_review.comment, 'A new review')

        self.assertIn('A new review', response.content.decode())
        expected_html = render_to_string(
            'home.html',
            {'new_review_text':  'A new review'}
        )
        self.assertEqual(response.content.decode(), expected_html)

    def test_home_page_only_saves_items_when_necessary(self):
        request = HttpRequest()
        home_page(request)
        self.assertEqual(Review.objects.count(), 0)

class reviewModelTest(TestCase):

    def test_saving_and_retrieving_Reviews(self):
        first_review = Review()
        first_review.comment = 'The first (ever) review'
        first_review.save()

        second_review = Review()
        second_review.comment = 'Review the second'
        second_review.save()

        saved_reviews = Review.objects.all()
        self.assertEqual(saved_reviews.count(), 2)

        first_saved_review = saved_reviews[0]
        second_saved_review = saved_reviews[1]
        self.assertEqual(first_saved_review.comment, 'The first (ever) review')
        self.assertEqual(second_saved_review.comment, 'Review the second')