from rest_framework import serializers
from readonlymodelviewSet.models import Collage


class CollageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collage
        fields = '__all__'