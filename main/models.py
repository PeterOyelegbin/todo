from django.db import models

# Create your models here.
class Todo(models.Model):
    status_options = [
        ('Pending', 'Pending'),
        ('Done', 'Done'),
    ]

    task = models.CharField(max_length=225)
    details = models.TextField()
    status = models.CharField(max_length=10, choices=status_options, default='Pending')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    # Sort post data in decending order
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.task
