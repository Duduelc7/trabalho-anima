from rest_framework import serializers
from aposentadoria.models import  *


class TrabalhoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trabalho
        fields = '__all__'