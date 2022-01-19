from django.db import models

# Create your models here.

class todoModel(models.Model):
    name = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    

    def __str__(self):
        return self.name
