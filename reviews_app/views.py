from django.shortcuts import render

from reviews_app.models import Review

def home_page(request):

    review = Review()
    review.comment = request.POST.get('review_text', '')
    review.save()

    return render(request, 'home.html', {
        'new_review_text': request.POST.get('review_text',''),
    })