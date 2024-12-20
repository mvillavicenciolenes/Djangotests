from django.shortcuts import render
from .models import ExampleModel

# Example view to render a list of ExampleModel
def home(request):
    examples = ExampleModel.objects.all()
    return render(request, 'home.html', {'examples': examples})