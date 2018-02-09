from django.shortcuts import render

# Create your views here.

def banners(request):
    return render(request, 'backend/banners/index.html')