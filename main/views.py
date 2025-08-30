from django.shortcuts import render

# Create your views here.
def indexPageView(request):
    return render(request, 'index.html')

def mlExamplePageView(request):
    return render(request, 'ml-example.html')