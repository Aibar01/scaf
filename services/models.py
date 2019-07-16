from django.db import models


class Service(models.Model):
    image = models.ImageField(upload_to='services/%Y/%m/%d/')
    title = models.CharField(max_length=100)
    description = models.TextField()
    in_img1 = models.ImageField(upload_to='services/in/%Y/%m/%d/', blank=True)
    in_img2 = models.ImageField(upload_to='services/in/%Y/%m/%d/', blank=True)
    in_img3 = models.ImageField(upload_to='services/in/%Y/%m/%d/', blank=True)
    associated = models.ImageField(upload_to='services/associated/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.title
