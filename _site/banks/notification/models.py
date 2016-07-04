from django.db import models

class Notification(models.Model):

    exam = models.CharField(max_length=255)
    qualification = models.CharField(max_length=255)
    vacancies = models.CharField(max_length=50)
    last_date = models.DateField()
    apply_now = models.CharField(max_length=255, blank=True, null=True)
    details = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.exam


class Category(models.Model):

    name = models.CharField(max_length=255)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class CurrentNews(models.Model):

    category = models.ForeignKey(Category)
    title = models.CharField(max_length=255)
    img = models.ImageField()
    source = models.CharField(max_length=100)
    published = models.DateField()
    description = models.TextField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title