from django.shortcuts import render

# Create your views here.
def practice1(request):
    return render(request, 'album/practice1.html')

def assignment1(request):
    return render(request, 'album/assignment1.html')

def assignment2(request):
    return render(request, 'album/assignment2.html')

def assignment3(request):
    return render(request, 'album/assignment3.html')
