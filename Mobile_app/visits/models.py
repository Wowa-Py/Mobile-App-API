from django.db import models

class Worker(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Store(models.Model):
    name = models.CharField(max_length=255)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Visit(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    visited_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
