import json
from rest_framework import generics, mixins, permissions
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from accounts.permissions import IsOwnerOrReadOnly
from .models import Product
from .serializers import ProductSerializer


class ProductAPIDetailView(
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin, 
    generics.RetrieveAPIView):

    permission_classes          = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    serializer_class            = ProductSerializer
    queryset                    = Product.objects.all()
    lookup_field                = 'slug'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



class ProductAPIView(
    mixins.CreateModelMixin, 
    generics.ListAPIView): 

    permission_classes          = [permissions.IsAuthenticatedOrReadOnly]
    # permission_classes          = [permissions.IsAuthenticated]
    serializer_class            = ProductSerializer
    passed_id                   = None
    search_fields               = ('user__username', 'description', 'user__email')
    ordering_fields             = ('user__username', 'timestamp')

    queryset                    = Product.objects.all()
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


