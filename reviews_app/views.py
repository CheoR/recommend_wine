from django.shortcuts import render, redirect

from reviews_app.models import Review

def home_page(request):
    if request.method == 'POST':
        Review.objects.create(comment=request.POST['review_text'])
        return redirect('/')

    return render(request, 'home.html')