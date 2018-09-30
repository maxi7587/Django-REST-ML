from django_rest_ml.tensorflow.models import TensorflowModel
from rest_framework import serializers


class TensorflowModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TensorflowModel
        fields = ('created', 'title', 'description', 'model_type')
