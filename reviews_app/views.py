from django.shortcuts import render

from reviews_app.models import Review

def home_page(request):
    if request.method == 'POST':
        new_review_text = request.POST['review_text']
        Review.objects.create(comment=new_review_text)
    else:
        new_review_text = ''

    return render(request, 'home.html', {
        'new_review_text': new_review_text,
    })