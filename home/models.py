from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # NEW field

    def __str__(self):
        return self.name

class Feedback(models.Model):
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment[:50]