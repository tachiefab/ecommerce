from rest_framework import generics
from .models import Category
from .serializers import CategorySerializer

class CategoryAPIView(generics.ListAPIView): 
    permission_classes          = []
    serializer_class            = CategorySerializer
    queryset                    = Category.objects.all()
