from rest_framework import serializers
from rest_framework.reverse import reverse as api_reverse
from accounts.serializers import UserPublicSerializer
from .models import Product
from categories.serializers import CategorySerializer

class ProductSerializer(serializers.ModelSerializer):
    uri             = serializers.SerializerMethodField(read_only=True)
    user            = UserPublicSerializer(read_only=True)
    class Meta:
        model = Product 
        fields =[
            'uri',
            'id',
            'user',
            'name',
            'slug',
            'description',
            'price',
            'product_category',
            'category',
            'image'
        ]
        read_only_fields = ['slug']

    def get_uri(self, obj):
        request = self.context.get('request')
        return api_reverse('api-products:detail', kwargs={"slug": obj.slug}, request=request)

    def validate(self, data):
        name = data.get("name")
        description = data.get("description", None)
        if description == "":
            description = None
        image = data.get("image", None)
        if name is None:
            raise serializers.ValidationError("Name is required.")
        return data



class ProductInlineUserSerializer(ProductSerializer):
    class Meta:
        model = Product 
        fields =[
            'uri',
            'id',
            'name',
            'description',
            'price',
            'product_category',
            'category',
            'image'
        ]