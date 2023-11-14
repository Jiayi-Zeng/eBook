from django.urls import path, include
from .models import MDPages
from rest_framework import serializers

# Serializers define the API representation.
class MDPageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MDPages
        fields = ['page_ptr_id','body']
