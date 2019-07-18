from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'website/home.html', locals())

def news(request):
    return render(request, 'website/news.html', locals())