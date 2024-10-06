from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.shortcuts import redirect
from .models import Job
from .forms import JobForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


def home(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/job_list.html', {'jobs': jobs})


def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk)
    return render(request, 'jobs/job_detail.html', {'job': job})


@login_required
def post_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = JobForm()
    return render(request, 'jobs/post_job.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after sign-up
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'jobs/signup.html', {'form': form})