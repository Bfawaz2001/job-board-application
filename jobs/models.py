from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Job(models.Model):
    EMPLOYMENT_TYPE_CHOICES = [
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
        ('contract', 'Contract')
    ]

    WORKING_CONDITION_CHOICES = [
        ('in_office', 'In Office'),
        ('remote', 'Remote'),
        ('hybrid', 'Hybrid')
    ]

    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    employment_type = models.CharField(max_length=50, choices=EMPLOYMENT_TYPE_CHOICES)
    working_condition = models.CharField(max_length=50, choices=WORKING_CONDITION_CHOICES)
    description = models.TextField()
    application_deadline = models.DateField()
    posted_on = models.DateTimeField(auto_now_add=True)

    recruiter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posted_jobs')

    def __str__(self):
        return self.title


class Profile(models.Model):
    USER_TYPE_CHOICES = (
        ('applicant', 'Applicant'),
        ('recruiter', 'Recruiter'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    bio = models.TextField(blank=True, null=True)  # Optional bio for user profiles

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Application(models.Model):
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    cover_letter = models.TextField(blank=True, null=True)
    applied_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.applicant.username} applied for {self.job.title}"
