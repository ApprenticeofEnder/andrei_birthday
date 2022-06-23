from django.db import models

# Create your models here.

class Memory(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    start_date = models.DateField()

    def __str__(self) -> str:
        return self.title