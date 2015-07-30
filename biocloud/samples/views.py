from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UploadSampleForm


@login_required
def sample_create(request):
    if request.method == 'POST':
        form = UploadSampleForm(request.POST, request.FILES)
        if form.is_valid():
            sample = form.save(commit=False)
            sample.owner = request.user
            sample.save()

            # Redirect to the document list after POST
            return redirect(sample_list)
    else:
        form = UploadSampleForm()

    return render(request, 'samples/sample_create.html', {'form': form})


@login_required
def sample_list(request):
    owned_samples = request.user.owned_samples.all()
    return render(request, 'samples/sample_list.html', {
        'owned_samples': owned_samples
    })
