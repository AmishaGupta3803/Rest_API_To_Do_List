from rest_framework import serializers
from .models import Task

class ToDoReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class ToDoWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        exclude = ('id',)