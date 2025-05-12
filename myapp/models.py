from django.db import models
# Create your models here.
class Task(models.Model):
    PRIORITY_CHOICES = [
        ("low", "Low"),
        ("medium", "Medium"),
        ("high", "High"),
    ]

    description = models.CharField(max_length=255, default="New task")  # required=True
    finish = models.BooleanField(default=False)
    due_date = models.DateTimeField(null=True, blank=True) 
    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default="low",
    )

    created_at = models.DateTimeField(auto_now_add=True)  # createdAt
    
    # def __str__(self):
    #     return self.__repr__()