from django.db import models

# Create your models here.
class list(models.Model):
    name = models.CharField(max_length = 20)
    email = models.CharField(max_length = 30)
    mobile_number = models.CharField(max_length = 30)
    work = models.TextField(max_length=50)

    def __str__(self):
        return self.name