from django.shortcuts import render

def home_page(request):
    return render(request, 'home.html', {
        'new_review_text': request.POST.get('review_text',''),
    })