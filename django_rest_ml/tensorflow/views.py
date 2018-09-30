from django.shortcuts import render

from rest_framework import viewsets
from django_rest_ml.tensorflow.models import TensorflowModel
from django_rest_ml.tensorflow.serializers import TensorflowModelSerializer

# Create your views here.

class TensorflowModelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tensorflow models to be viewed or edited.
    """
    queryset = TensorflowModel.objects.all().order_by('-created')
    serializer_class = TensorflowModelSerializer
