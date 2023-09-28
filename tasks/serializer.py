from rest_framework import serializers
from .models import Juegos


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Juegos
        fields = '__all__'