from django.shortcuts import render

# Create your views here.

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')

def simple_page(request):
    return render(request, 'pages/simple.html')
