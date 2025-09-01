from django.shortcuts import render
from .modules.linearRegression import LinearRegressionModel

from .forms import LinearRegressionForm

# Create your views here.
def indexPageView(request):
    return render(request, 'index.html')

def mlExamplePageView(request):
    return render(request, 'ml-example.html')

def linearRegressionView(request):
    mlModel = LinearRegressionModel()
    context = {
        'graph' : mlModel.genGraph(),
        'resultY' : None
    }

    if request.method == "POST":
        form = LinearRegressionForm(request.POST)
        if form.is_valid():
            context['submittedX'] = form.cleaned_data["submitted_x"]
            context['resultY'] = mlModel.genYValue(form.cleaned_data["submitted_x"])
    else:
        form = LinearRegressionForm()

    context['form'] = form
    
    return render(request, 'machine-learning/linear-regression.html', context)