from django.shortcuts import render

finches = [
    {'name': 'Henry', 'breed': 'American Goldfinch', 'description': 'a shining beacon of light', 'age': 3},
    {'name': 'Sawyer', 'breed': 'Red Crossbill', 'description': 'gentle and loving', 'age': 2},
]

# Create your views here.
def home(request):
    # return render(request, 'home.html')
    return render(request, 'about.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', {
        'finches': finches
    })