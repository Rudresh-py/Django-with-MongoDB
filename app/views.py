from app.serializers import UserRegistrationSerializer, ProductSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework.generics import ListAPIView
from app.models import Product


class RegisterView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"messages": "User successfully registered"})
        return Response(serializer.errors, status=400)


class UsersView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer


class ProductCreate(APIView):
    def post(self, request):
        serializer = ProductSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"messages": "Product create successfully"})
        return Response(serializer.errors, status=400)

    def put(self, request, pk=None):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializers(instance=product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"messages": "Product create successfully"})
        return Response(serializer.errors, status=400)
