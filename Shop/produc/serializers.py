from rest_framework import serializers
from .models import Produc

class ProducSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produc
        fields = (
            "id",
            "clasific",
            "name",
            "price",
            "image",
            "supplier",
    )