from django.shortcuts import render

from rest_framework import viewsets
from django_rest_ml.sklearn.models import SklearnModel
from django_rest_ml.sklearn.serializers import SklearnModelSerializer

# Create your views here.

class SklearnModelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows sklearn models to be viewed or edited.
    """
    queryset = SklearnModel.objects.all().order_by('-created')
    serializer_class = SklearnModelSerializer
