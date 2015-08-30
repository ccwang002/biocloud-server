from django.shortcuts import render, redirect
from .forms import ExampleForm
import logging

logger = logging.getLogger(__name__)

# Create your views here.
def example_form(request):
    logger.info('Get request')
    if request.method == 'POST':
        form = ExampleForm(data=request.POST)
        if form.is_valid():
            return redirect('home')

    else:
        form = ExampleForm()
    return render(request, 'play_form/example_form.html', {
        'form': form
    })

def example_multiform(request):
    logger.info('Multiform')
    return redirect('home')
