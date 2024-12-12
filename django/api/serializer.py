from rest_framework import serializers
from .models import programmer
from .models import student

class ProgrammerSerializer(serializers.ModelSerializer):
    class Meta:
        model=programmer
        fields= '__all__' 
        
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=student
        fields= '__all__' 