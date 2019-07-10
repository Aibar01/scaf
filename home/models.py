from django.db import models


class Engineer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='engineers/%Y/%m/%d')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Review(models.Model):
    full_name = models.CharField(max_length=100)
    description = models.TextField()
    hire_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
