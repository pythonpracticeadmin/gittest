from rest_framework import serializers
from .models import menmodel

class menmodelapi(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = menmodel