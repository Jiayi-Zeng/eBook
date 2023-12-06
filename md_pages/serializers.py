from django.urls import path, include
from .models import MDPages
from rest_framework import serializers
from wagtail.models import Page

# Serializers define the API representation.
class MDPageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MDPages
        fields = ['page_ptr_id','body']

class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ['id', 'title', 'owner_id', 'url_path', 'slug', 'numchild', 'depth']  # 可根据需要调整字段

