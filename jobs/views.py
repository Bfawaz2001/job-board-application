from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Job, Profile
from .forms import JobForm, SignUpForm, ProfileForm, ApplicantProfileForm
from .forms import ApplicationForm
from django.contrib.auth.forms import UserChangeForm
from django.db.models import Q


# Home view displaying job listings
def home(request):
    jobs = Job.objects.all()

    # Get search query and filters from request GET parameters
    search_query = request.GET.get('search', '')
    employment_type = request.GET.get('employment_type', '')
    working_condition = request.GET.get('working_condition', '')
    location = request.GET.get('location', '')

    # Apply filters if provided
    if search_query:
        jobs = jobs.filter(Q(title__icontains=search_query) | Q(company__icontains=search_query))
    if employment_type:
        jobs = jobs.filter(employment_type=employment_type)
    if working_condition:
        jobs = jobs.filter(working_condition=working_condition)
    if location:
        jobs = jobs.filter(location__icontains=location)

    return render(request, 'jobs/job_list.html', {'jobs': jobs})


# Job detail view
def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk)
    return render(request, 'jobs/job_detail.html', {'job': job})


# View to post a new job (for recruiters)
@login_required
def post_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.recruiter = request.user  # Set the recruiter field to the current user
            job.save()
            return redirect('home')
    else:
        form = JobForm()
    return render(request, 'jobs/post_job.html', {'form': form})

# Sign-up view to register new users
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.profile.user_type = form.cleaned_data.get('user_type')
            user.profile.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'jobs/signup.html', {'form': form})


# Profile view for the current user
@login_required
def view_profile(request):
    return render(request, 'jobs/profile.html', {'profile': request.user.profile})


# Edit profile view
@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('view_profile')
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'jobs/edit_profile.html', {'form': form})


@login_required
def edit_job(request, pk):
    job = get_object_or_404(Job, pk=pk)
    if request.user.profile.user_type != 'recruiter' or job.recruiter != request.user:
        return redirect('home')

    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('my_job_postings')
    else:
        form = JobForm(instance=job)

    return render(request, 'jobs/edit_job.html', {'form': form, 'job': job})


@login_required
def my_job_postings(request):
    if request.user.profile.user_type != 'recruiter':
        return redirect('home')

    jobs = Job.objects.filter(recruiter=request.user)  # Only fetch jobs posted by the current recruiter
    return render(request, 'jobs/my_job_postings.html', {'jobs': jobs})


@login_required
def delete_job(request, pk):
    job = get_object_or_404(Job, pk=pk)
    if request.user.profile.user_type != 'recruiter' or job.recruiter != request.user:
        return redirect('home')

    if request.method == 'POST':
        job.delete()
        return redirect('my_job_postings')


@login_required
def apply_for_job(request, pk):
    job = get_object_or_404(Job, pk=pk)
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.applicant = request.user
            application.job = job
            application.save()
            return redirect('home')
    else:
        form = ApplicationForm()

    return render(request, 'jobs/apply_for_job.html', {'form': form, 'job': job})


@login_required
def update_profile(request):
    if request.method == 'POST':
        form = ApplicantProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ApplicantProfileForm(instance=request.user)

    return render(request, 'jobs/update_profile.html', {'form': form})


def job_list(request):
    jobs = Job.objects.all()  # Initially fetch all jobs

    # Get the query parameters for search and filters
    title_query = request.GET.get('title')
    location_query = request.GET.get('location')
    employment_type_query = request.GET.get('employment_type')
    working_condition_query = request.GET.get('working_condition')

    # Filter by title if provided
    if title_query:
        jobs = jobs.filter(title__icontains=title_query)

    # Filter by location if provided
    if location_query:
        jobs = jobs.filter(location__icontains=location_query)

    # Filter by employment type if provided
    if employment_type_query:
        jobs = jobs.filter(employment_type=employment_type_query)

    # Filter by working condition if provided
    if working_condition_query:
        jobs = jobs.filter(working_condition=working_condition_query)

    return render(request, 'jobs/job_list.html', {'jobs': jobs})
