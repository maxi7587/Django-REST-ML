from django_rest_ml.sklearn.models import SklearnModel
from rest_framework import serializers


class SklearnModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SklearnModel
        fields = ('created', 'title', 'description', 'model_type')
