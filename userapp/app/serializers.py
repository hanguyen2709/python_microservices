from rest_framework import serializers
from .models import CoreUsers

class CoreUsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = CoreUsers
        fields = '__all__'
