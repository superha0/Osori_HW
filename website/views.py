from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'website/index.html',{})

def test_board(request):
	return render(request, 'website/test_board.html', {})

