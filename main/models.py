from django.db import models

# Create your models here.
class Projects(models.Model):
    project_name = models.CharField(max_length=30)
    project_description = models.CharField(max_length=100)
    project_link = models.URLField(max_length=30)


 
