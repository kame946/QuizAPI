from django.db import models

# Create your models here.

class Quiz(models.Model):
    STATUS_CHOICES = [
        ('inactive', 'Inactive'),
        ('active', 'Active'),
        ('finished', 'Finished'),
    ]

    question = models.TextField()
    options = models.JSONField()
    right_answer = models.PositiveIntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='inactive')
    

    def __str__(self):
        return self.question
