from django.db import models


class Testimonial(models.Model):

    name = models.CharField(max_length=255)
    college = models.CharField(max_length=255, null=True, blank=True)
    photo = models.ImageField()
    description = models.TextField()
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Career(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=12)
    subject = models.CharField(max_length=255)
    resume = models.FileField()
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.first_name + self.last_name
