from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from .models import Job


def home(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/job_list.html', {'jobs': jobs})


def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk)
    return render(request, 'jobs/job_detail.html', {'job': job})
