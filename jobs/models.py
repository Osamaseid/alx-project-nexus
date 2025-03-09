from django.db import models

# Create your models here.
class Job(models.Model):
    
    EXPERIENCE_LEVELS = [
        ('entry', 'Entry Level'),
        ('mid', 'Mid Level'),
        ('senior', 'Senior Level'),
    ]

    title = models.CharField(max_length=255, db_index=True)  # Indexed for search speed
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255, db_index=True)  # Indexed
    category = models.CharField(max_length=100, db_index=True)  # Indexed
    experience_level = models.CharField(max_length=10, choices=EXPERIENCE_LEVELS, default='entry')

    description = models.TextField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    posted_by = models.ForeignKey('users.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="applications")
    applicant = models.ForeignKey('users.User', on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.TextField()
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.applicant.username} - {self.job.title}"

