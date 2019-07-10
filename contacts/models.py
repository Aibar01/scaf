from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    hire_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-hire_date']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
