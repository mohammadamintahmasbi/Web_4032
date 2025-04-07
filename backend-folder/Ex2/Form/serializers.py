from rest_framework import serializers
from .models import Form
class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = ('first_name', 'last_name', 'age', 'education_degree')