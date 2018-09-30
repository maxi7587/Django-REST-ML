from django.db import models

# Create your models here.

classification = "classification"
regression = "regression"

SKLEARN_MODEL_CHOICES = ((classification, "classification"),(regression, "regression"),)

class SklearnModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField()
    model_type = models.CharField(choices=SKLEARN_MODEL_CHOICES, default='classification', max_length=100)

    class Meta:
        ordering = ('created',)
