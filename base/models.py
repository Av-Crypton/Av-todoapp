from django.db import models
import uuid

# Create your models here.
class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    time = models.TimeField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    creation_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title