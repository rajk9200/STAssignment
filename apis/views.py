from django.contrib.auth import authenticate

from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from products.models import Category,Product

from .serializers import CategorySerializer,ProductSerializer
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        else:
            return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)




class CategoryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        if pk:
            category = get_object_or_404(Category, pk=pk)
            serializer = CategorySerializer(category)
            return Response({
                "data": serializer.data,
                "message": "Category retrieved successfully."
            }, status=status.HTTP_200_OK)

        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response({
            "data": serializer.data,
            "message": "Categories retrieved successfully."
        }, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "data": serializer.data,
                "message": "Category created successfully."
            }, status=status.HTTP_201_CREATED)
        return Response({
            "data": {},
            "message": "Failed to create category."
        }, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        serializer = CategorySerializer(category, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "data": serializer.data,
                "message": "Category updated successfully."
            }, status=status.HTTP_200_OK)
        return Response({
            "data": {},
            "message": "Failed to update category."
        }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        category.delete()
        return Response({
            "data": {},
            "message": "Category deleted successfully."
        }, status=status.HTTP_204_NO_CONTENT)





class ProductView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        if pk:
            product = get_object_or_404(Product, pk=pk)
            serializer = ProductSerializer(product)
            return Response({
                "data": serializer.data,
                "message": "Product retrieved successfully."
            }, status=status.HTTP_200_OK)

        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response({
            "data": serializer.data,
            "message": "Products retrieved successfully."
        }, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({
                "data": serializer.data,
                "message": "Product created successfully."
            }, status=status.HTTP_201_CREATED)
        return Response({
            "data": {},
            "message": "Failed to create product."
        }, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        if product.user != request.user:
            return Response({
                "data": {},
                "message": "You do not have permission to edit this product."
            }, status=status.HTTP_403_FORBIDDEN)

        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "data": serializer.data,
                "message": "Product updated successfully."
            }, status=status.HTTP_200_OK)
        return Response({
            "data": {},
            "message": "Failed to update product."
        }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        if product.user != request.user:
            return Response({
                "data": {},
                "message": "You do not have permission to delete this product."
            }, status=status.HTTP_403_FORBIDDEN)

        product.delete()
        return Response({
            "data": {},
            "message": "Product deleted successfully."
        }, status=status.HTTP_204_NO_CONTENT)
