from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/%Y/%m/%d/')
    hire_date = models.DateField()

    def __str__(self):
        return self.title
