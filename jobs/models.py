from django.db import models

# Create your models here.
from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    employment_type = models.CharField(max_length=50, choices=[('Full-time', 'Full-time'), ('Part-time', 'Part-time'), ('Contract', 'Contract')])
    posted_on = models.DateField(auto_now_add=True)
    application_deadline = models.DateField()

    def __str__(self):
        return self.title
