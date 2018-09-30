from django.db import models

# Create your models here.

classification = "classification"
regression = "regression"

TENSORFLOW_MODEL_CHOICES = ((classification, "classification"),(regression, "regression"),)

class TensorflowModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField()
    model_type = models.CharField(choices=TENSORFLOW_MODEL_CHOICES, default='classification', max_length=100)

    class Meta:
        ordering = ('created',)
