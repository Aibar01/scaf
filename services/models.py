from django.db import models


class Service(models.Model):
    image = models.ImageField(upload_to='services/%Y/%m/%d/')
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title
