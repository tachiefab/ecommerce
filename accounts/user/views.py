from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, pagination
from rest_framework.response import Response
from accounts.permissions import AnonPermissionOnly
from products.serializers import ProductInlineUserSerializer
from products.views import ProductAPIView
from products.models import Product
from .serializers import UserDetailSerializer

User = get_user_model()

class UserDetailAPIView(generics.RetrieveAPIView):
    queryset            = User.objects.filter(is_active=True)
    serializer_class    = UserDetailSerializer
    lookup_field        = 'username'

    def get_serializer_context(self):
        return {'request': self.request}


class UserProductAPIView(ProductAPIView):
    serializer_class            = ProductInlineUserSerializer
    
    def get_queryset(self, *args, **kwargs):
        username = self.kwargs.get("username", None)
        if username is None:
            return Product.objects.none()
        return Product.objects.filter(user__username=username)

    def post(self, request, *args, **kwargs):
        return Response({"detail": "Not allowed here"}, status=400)
        